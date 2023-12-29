import time
from datetime import datetime


class BaseDecorator:

    def __init__(self, my_function):
        self._function = my_function
        self._info = list()

    def __call__(self, *args, **kwargs):
        self.decorate()
        result = self._function(*args, **kwargs)
        self.keep_history()
        self.log_info(*args)
        return result

    def log_info(self, *args):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self._info.append(f"{current_time}: function {self._function.__name__} called with arguments {args}")
        print(self._info)

    def decorate(self):
        pass

    def keep_history(self):
        pass



class TimerDecorator(BaseDecorator):

    @property
    def __name__(self):
        return self._function.__name__

    def decorate(self):
        self.start_time = time.perf_counter()

    def keep_history(self):
        self.runtime = time.perf_counter() - self.start_time



class HtmlDecorator(BaseDecorator):

    def decorate(self):
        pass

    def keep_history(self):
        print(f"<html><body>{self._function.runtime:.10f}</body></html>")
