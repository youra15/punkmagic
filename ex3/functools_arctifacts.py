import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    if operation not in operations:
        raise ValueError(f"Unknown operation: '{operation}'")
    if not spells:
        return 0
    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": functools.partial(base_enchantment, 50, "fire"),
        "ice": functools.partial(base_enchantment, 50, "ice"),
        "lightning": functools.partial(base_enchantment, 50, "lightning"),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register
    def cast_damage(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register
    def cast_enchantment(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register
    def cast_multi(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast


def enchant(power: int, element: str, target: str) -> str:
    return f"{element.capitalize()} enchantment ({power}) on {target}"


def main() -> None:
    spells = [10, 20, 30, 40]

    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print(f"Min: {spell_reducer(spells, 'min')}")
    print(f"Empty: {spell_reducer([], 'add')}")
    try:
        spell_reducer(spells, "divide")
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting partial enchanter...")
    enchanters = partial_enchanter(enchant)
    for enchanter in enchanters.values():
        print(enchanter("Sword"))

    print("\nTesting memoized fibonacci...")
    for n in [0, 1, 10, 15]:
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print(f"Cache: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fireball", "heal", "shield"]))
    print(dispatcher(3.14))


if __name__ == "__main__":
    main()
