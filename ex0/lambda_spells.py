def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: "* " + s + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
    strongest = max(mages, key=lambda m: m['power'])
    weakest = min(mages, key=lambda m: m['power'])
    total = sum(map(lambda m: m['power'], mages))
    return {
        'max_power': strongest['power'],
        'min_power': weakest['power'],
        'avg_power': round(total / len(mages), 2),
    }


def main() -> None:
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'staff'},
        {'name': 'Shadow Dagger', 'power': 60, 'type': 'weapon'},
    ]
    mages = [
        {'name': 'Merlin', 'power': 95, 'element': 'light'},
        {'name': 'Morgana', 'power': 78, 'element': 'shadow'},
        {'name': 'Gandalf', 'power': 64, 'element': 'fire'},
    ]

    print("Testing artifact sorter...")
    s = artifact_sorter(artifacts)
    print(
        f"{s[0]['name']} ({s[0]['power']} power) comes before "
        f"{s[1]['name']} ({s[1]['power']} power)"
    )

    print("\nTesting power filter...")
    print(list(map(lambda m: m['name'], power_filter(mages, 70))))

    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(["fireball", "heal", "shield"])))

    print("\nTesting mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
