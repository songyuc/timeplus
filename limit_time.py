import inspect
import threading
import time


class RunTimeoutError(Exception):
    pass


class StartTimeRecorder:
    _instances = {}

    @classmethod
    def get_start_time(cls, identifier):
        assert isinstance(identifier, tuple)
        if identifier not in cls._instances:
            cls._instances[identifier] = time.perf_counter()
        return cls._instances[identifier]


def max_time(t):
    # identifier = (thread_id, stack_depth, filename, line_number, col_offset)
    identifier = (threading.current_thread().ident,
                  *((info.filename, info.lineno, info.positions.col_offset) for info in inspect.stack()))

    # 这里使用 Class: StartTimeRecorder 来记录状态，因为python并不推荐在函数中定义静态变量，所以我们设计在类中定义静态变量
    if (val := time.perf_counter() - StartTimeRecorder.get_start_time(identifier)) > t:
        print(val)
        raise RunTimeoutError(f"Operation timed out after {t} seconds")
    return True
