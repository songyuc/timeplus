import threading
import time
import weakref
import inspect


class RunTimeoutError(Exception):
    pass


def check_if_program_started():
    # 实现检查程序是否启动的逻辑
    # 这里只是一个示例
    return False


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


def main():
    # 使用示例
    try:
        i = 0
        while max_time(3):
            # 逻辑检查程序是否已启动
            start_success = check_if_program_started()
            if start_success:
                print("Program started successfully.")
                break
            # 演示目的的休眠
            time.sleep(1)

            i += 1
            print(i)
    except RunTimeoutError as e:
        print(e)

    try:
        j = 0
        while max_time(3):  # 内部的 max_time
            time.sleep(1)
            j += 1
            print(f"second-j: {j}")
    except RunTimeoutError as e:
        print(e)

    return 0


if __name__ == '__main__':
    main()
