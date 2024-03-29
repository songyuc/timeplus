import inspect


def main(a=0):
    assert a == 0

    current_frame = inspect.currentframe()
    frame_info = inspect.getframeinfo(current_frame)
    stack = inspect.stack()
    identifier = (
        frame_info.filename,
        frame_info.lineno,
        frame_info.function,
        frame_info.index,
        frame_info.code_context[0].strip(),
        stack[0].positions.col_offset,
    )

    print(identifier)

    return 0


if __name__ == '__main__':
    main(main())
