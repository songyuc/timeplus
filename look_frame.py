import inspect


def main(a=0):
    assert a == 0
    stack = inspect.stack()
    identifier = (
        stack[1].filename, stack[1].lineno, stack[0].function, stack[0].index, stack[1].code_context[0].strip(),
        stack[1].positions.col_offset,
        inspect.currentframe().f_back.f_lasti)
    print(identifier)
    return 0


if __name__ == '__main__':
    main(main())
    main()
    main()
