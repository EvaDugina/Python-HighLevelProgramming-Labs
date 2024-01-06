import time
from datetime import datetime


class BaseDecorator:
    def __init__(self, my_function):
        self._function = my_function
        self.list_info = list()

    def __call__(self, *args, **kwargs):
        self.decorate(*args, **kwargs)
        self.log_info(*args)
        print()

    @property
    def __name__(self):
        return self._function.__name__

    def decorate(self, *args, **kwargs):
        pass

    def log_info(self, *args):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S.%f")
        self.list_info.append(f"{current_time}: function {self._function.__name__} called with arguments {args}")
        print(self.list_info)


class TimerDecorator(BaseDecorator):

    @property
    def __name__(self):
        return self._function.__name__

    def decorate(self, *args, **kwargs):
        start_time = time.perf_counter()
        result = self._function(*args, **kwargs)
        self.runtime = time.perf_counter() - start_time

        return result


class HtmlDecorator(BaseDecorator):

    def decorate(self, *args, **kwargs):
        result = self._function(*args, **kwargs)
        print(f"<html><body>{self._function.runtime:.10f}</body></html>")
        return result