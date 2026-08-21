from collections.abc import Callable
from typing import Protocol


class Operation[**P, R](Protocol):
    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R: ...


def cacher[**P, R](callback: Operation[P, R]) -> Callable[P, R]:
    cached_params: dict[tuple[object, ...], R] = {}

    def closure(*args: P.args, **kwargs: P.kwargs) -> R:
        if args in cached_params:
            result = cached_params[args]
            print(f"Cacher found result {result!r}")
        else:
            result = callback(*args, **kwargs)
        cached_params[args] = result

        return result

    return closure


def operation(*args: str) -> list[str]:
    import time

    values: list[str] = []

    for arg in args:
        print(f"Fazendo algo complexo ou demorado com {arg!r}...")
        time.sleep(1)
        values.append(arg)

    return values


# print("\nCacher")
# operation_cached = cacher(operation)

# op1 = operation_cached("a", "b", "c")
# op2 = operation_cached("a", "b", "c")  # em cache
# op2 = operation_cached("a", "b", "c")  # em cache

# op4 = operation_cached("b", "b", "c")
# op5 = operation_cached("b", "b", "c")  # em cache


@cacher
def get_from_db(id: int, /) -> str:
    import time

    names = ["Luiz", "Maria", "Helena", "Letícia"]

    print(f"Returning value for ID {id}")
    time.sleep(2)
    return names[id]


print("\nCacher Decorator")

print(get_from_db(1))
print(get_from_db(1))
print(get_from_db(0))
print(get_from_db(2))
print(get_from_db(0))
print(get_from_db(2))
print(get_from_db(0))
print(get_from_db(2))
print(get_from_db(0))
print(get_from_db(2))

# ** Introspecção de closures