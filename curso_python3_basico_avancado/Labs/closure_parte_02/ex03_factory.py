from collections.abc import Callable

# Factory (fábrica de funções)
def make_multiplier(multiplier: float, /) -> Callable[[float], float]:
    def multiplier_times(multiplicand: float, /) -> float:
        return multiplicand * multiplier

    return multiplier_times


print("\nMultiplicadores")
times_two = make_multiplier(2)  # Função interna precisará lembrar do 2
times_three = make_multiplier(3)  # Nesse caso do 3

print("3 * 2 =   ", times_two(3))  # 3 * [2] = 6 - [2] lembrado
print("3 * 5 =   ", times_three(5))  # 5 * [3] = 15 - [3] lembrado
