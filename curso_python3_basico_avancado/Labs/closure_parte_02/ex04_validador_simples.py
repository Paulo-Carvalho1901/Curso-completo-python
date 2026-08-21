from collections.abc import Callable

# Validador simples
def make_lt_checker(min_value: int) -> Callable[[int], bool]:
    def is_lt(value: int) -> bool:
        return value < min_value

    return is_lt


print("\nValidatores simples")
lt_ten = make_lt_checker(10)  # 10 precisa ser lembrado

print("30 < 10   ", lt_ten(30))  # 30 é menor do que 10? False
print("9 < 10   ", lt_ten(9))  # 9 é menor do que 10? True
