class Logger:
    _green = "\033[32m"
    _red = "\033[31m"
    _orange = "\033[33m"
    _reset = "\033[39m"

    def info(self, *args):
        print(f"{self._green}INFO{self._reset}:\t ", *args)

    def error(self, *args):
        print(f"{self._red}ERROR{self._reset}:\t ", *args)

    def warn(self, *args):
        print(f"{self._orange}WARN{self._reset}:\t ", *args)
