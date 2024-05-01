import memory_profiler
from typing import Callable


def memory_usage_decorator_factory(print_delta: bool = False, return_delta: bool = True) -> Callable:
    """Decorator factory to measure a method's memory usage."""
    def decorator(method: Callable) -> Callable:
        def inner(*args, **kwargs) -> float | None:
            mem_usage_before = memory_profiler.memory_usage()[0]
            method(*args, **kwargs)
            mem_usage_after = memory_profiler.memory_usage()[0]

            delta: float = mem_usage_after - mem_usage_before

            if print_delta:
                print(f"Memory usage of {method.__name__}: {delta} MB")

            if return_delta:
                return delta

        return inner

    return decorator
