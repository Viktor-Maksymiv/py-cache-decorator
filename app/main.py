from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_list = {}

    def inner(*args) -> Any:
        if args in result_list:
            print("Getting from cache")
            return result_list[args]
        else:
            print("Calculating new result")
            result_list[args] = func(*args)
            return result_list[args]
    return inner
