import sys
from typing import Callable


def program_exiter(condition: bool, callback: Callable):
    if (condition):
        callback()
        sys.exit(-1)
