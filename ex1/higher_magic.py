from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1) or not callable(spell2):
        raise TypeError("spell_combiner expects two callables")

    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            result = spell(target, power)
        else:
            result = "Spell fizzled"
        return result
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} with {power} armor"


def is_strong_enough(target: str, power: int) -> bool:
    return power >= 50


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print("Combined spell result:", ", ".join(combined("Dragon", 10)))

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print("Original:", fireball("Dragon", 10))
    print("Amplified:", mega_fireball("Dragon", 10))

    print("\nTesting conditional caster...")
    safe_fireball = conditional_caster(is_strong_enough, fireball)
    print("Power 80:", safe_fireball("Goblin", 80))
    print("Power 20:", safe_fireball("Goblin", 20))

    print("\nTesting spell sequence...")
    combo = spell_sequence([shield, mega_fireball, heal])
    for result in combo("Knight", 15):
        print("-", result)

    print("\nTesting callable() check...")
    try:
        spell_combiner(fireball, "not a spell")
    except TypeError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
