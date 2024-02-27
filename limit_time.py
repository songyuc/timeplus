import inspect
import threading
import time


class RunTimeoutError(Exception):
    pass


class LimitedTime:
    _instances = {}

    def __new__(cls, identifier):
        if identifier not in cls._instances:
            cls._instances[identifier] = super(LimitedTime, cls).__new__(cls)
            # raise NotImplementedError
        return cls._instances[identifier]

    def __init__(self, timeout_seconds):
        if not hasattr(self, 'initialized'):
            self.timeout_seconds = timeout_seconds
            self.start_time = time.perf_counter()
            self.initialized = True

    def __next__(self):
        if time.perf_counter() - self.start_time > self.timeout_seconds:
            raise RunTimeoutError(f"Operation timed out after {self.timeout_seconds} seconds")
        return self


def max_time(t):
    thread_id = threading.get_ident()
    stack_depth = len(inspect.stack())
    frame = inspect.currentframe().f_back
    line_number = frame.f_lineno
    filename = frame.f_code.co_filename
    identifier = (thread_id, stack_depth, line_number, filename)
    counter = LimitedTime(identifier)
    if time.perf_counter() - counter.start_time > t:
        raise RunTimeoutError(f"Operation timed out after {t} seconds")
    return True
