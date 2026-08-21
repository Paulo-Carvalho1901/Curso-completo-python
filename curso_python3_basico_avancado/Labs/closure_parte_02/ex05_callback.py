from collections.abc import Callable


def with_callback(value: str, callback: Callable[[str], str]) -> Callable[[], str]:
    # Você também poderia realizar algo aqui
    def runner() -> str:
        print(f"Realizando alguma operação com o valor {value!r}")
        return callback(value)

    return runner


def my_callback(value: str) -> str:
    print(f"Valor {value!r} recebido no callback")
    return value + " (callback executed)"


print("\nCallback")

execute_operation = with_callback("## Exemplo ##", callback=my_callback)
result = execute_operation()
print(f"Callback:    {result!r}")
