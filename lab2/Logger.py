from datetime import datetime


class MyLogger(object):

    def __init__(self, path: str):
        self._file = open(path, "a", encoding="utf-8")

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(MyLogger, cls).__new__(cls)
        return cls.instance

    def __del__(self):
        self._file.close()

    def get_current_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time

    def write_to_log(self, message: str, status: str):
        self._file.write(f"[{status}] {self.get_current_time()}: {message}\n")


    def critical(self, message: str):
        self.write_to_log(message, "CRITICAL")

    def debug(self, message: str):
        self.write_to_log(message, "DEBUG")

    def error(self, message: str):
        self.write_to_log(message, "ERROR")

    def warn(self, message: str):
        self.write_to_log(message, "WARN")

    def info(self, message: str):
        self.write_to_log(message, "INFO")