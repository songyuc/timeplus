import time

from limit_time import max_time, RunTimeoutError


def check_if_program_started():
    # 实现检查程序是否启动的逻辑
    # 这里只是一个示例
    return False


def main(x=0):
    assert x == 0
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
            print(f"second: {j}")
    except RunTimeoutError as e:
        print(e)

    return 0


if __name__ == '__main__':
    main() + main()

