def compose(*fns):
    def composed():
        for fn in fns:
            fn()

    return composed
