import time
from datetime import datetime


class BaseDecorator:
    def __init__(self, my_function):
        self._function = my_function
        self.list_info = list()

    def _logInfo(self, *args):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.list_info.append(f"{current_time}: function {self._function.__name__} called with arguments {args}")
        print(self.list_info)


class TimerDecorator(BaseDecorator):

    @property
    def __name__(self):
        return self._function.__name__

    def __call__(self, *args, **kwargs):
        self.start_time = time.perf_counter()
        result = self._function(*args, **kwargs)
        self.runtime = time.perf_counter() - self.start_time
        self._logInfo(*args)
        return result


class HtmlDecorator(BaseDecorator):

    def __call__(self, *args, **kwargs):
        result = self._function(*args, **kwargs)
        self._logInfo(*args)
        print(f"<html><body>{self._function.runtime:.10f}</body></html>")
        return result