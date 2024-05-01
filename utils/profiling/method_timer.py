from timeit import default_timer
from typing import Callable


def execution_time_decorator_factory(print_delta: bool = False, return_delta: bool = True) -> Callable:
    """Decorator factory to measure a method's execution time."""

    def decorator(method: Callable) -> Callable:
        def inner(*args, **kwargs) -> float | None:

            start_time = default_timer()
            method(*args, **kwargs)
            end_time = default_timer()
            delta: float = end_time - start_time

            if print_delta:
                print(f"Execution time of {method.__name__}: {delta} ")

            if return_delta:
                return delta

        return inner

    return decorator
