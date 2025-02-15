from colorama import Fore, Back, Style

class FileFormatNotSupported(Exception):
    def __init__(self, format, context) -> None:
        message = f" '{format}' file format is not supported -> {context}"
        super().__init__(message)

def warn(context, title=None, message=None):
    print(Fore.YELLOW + f"{context} [{title}] : " + Fore.WHITE + f"{message}" + Fore.RESET)
