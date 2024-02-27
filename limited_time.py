import time

from exp.while_wait_func import RunTimeoutError


class LimitedTime:
    _instances = {}

    def __new__(cls, thread_id):
        if thread_id not in cls._instances:
            cls._instances[thread_id] = super(LimitedTime, cls).__new__(cls)
        return cls._instances[thread_id]

    def __init__(self, timeout_seconds):
        if not hasattr(self, 'initialized'):
            self.timeout_seconds = timeout_seconds
            self.start_time = time.time()  # 将 start_time 移动到这里
            self.initialized = True

    def __next__(self):
        if time.time() - self.start_time > self.timeout_seconds:
            raise RunTimeoutError(f"Operation timed out after {self.timeout_seconds} seconds")
        return self
