from collections import Counter


def nalozi_besede():
    with open("besede.txt", encoding="utf-8") as f:
        return [beseda.strip().lower() for beseda in f]


def relativne_frekvence(besede):
    # Counter je nekakšen slovar:
    # https://realpython.com/python-counter/
    stevec_pojavitev = Counter()
    for beseda in besede:
        stevec_pojavitev.update(beseda)
    n = sum(stevec_pojavitev.values())
    frekvence = {}
    for crka, stevec in sorted(stevec_pojavitev.items(), key=lambda par: -par[1]):
        frekvence[crka] = stevec / n
    with open("frekvence.csv", "w", encoding="utf-8") as f:
        for crka, frek in frekvence.items():
            print(f"{crka},{frek:.2e}", file=f)


vse_besede = nalozi_besede()
relativne_frekvence(vse_besede)
