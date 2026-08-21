from collections.abc import Callable

type Logger = callable[[str], None]
