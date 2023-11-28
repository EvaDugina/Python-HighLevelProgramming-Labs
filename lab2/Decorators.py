import time
from datetime import datetime


class BaseDecorator:

    _function = None
    _info = list()

    def __init__(self, my_function):
        self._function = my_function
        self._info = list()

    def log_info(self, *args):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self._info.append(f"{current_time}: function {self._function.__name__} called with arguments {args}")
        print(self._info)


class TimerDecorator(BaseDecorator):

    @property
    def __name__(self):
        return self._function.__name__

    def __call__(self, *args, **kwargs):
        self.start_time = time.perf_counter()
        result = self._function(*args, **kwargs)
        self.runtime = time.perf_counter() - self.start_time
        self.log_info(*args)
        return result



class HtmlDecorator(BaseDecorator):

    def __call__(self, *args, **kwargs):
        result = self._function(*args, **kwargs)
        self.log_info(*args)
        print(f"<html><body>{self._function.runtime:.10f}</body></html>")
        return result