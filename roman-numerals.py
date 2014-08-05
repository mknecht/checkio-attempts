# I 1 (unus)
# V 5 (quinque)
# X 10 (decem)
# L 50 (quinquaginta)
# C 100 (centum)
# D 500 (quingenti)
# M 1,000 (mille)

place2symbol = "IXCM"

replacements = [
    ("I" * 9, "IX"),
    ("I" * 5, "V"),
    ("I" * 4, "IV"),
    ("X" * 9, "XC"),
    ("X" * 5, "L"),
    ("X" * 4, "XL"),
    ("C" * 9, "CM"),
    ("C" * 5, "D"),
    ("C" * 4, "CD"),
]


def checkio(number):
    snumber = str(number)
    replaceable = "".join([
        place2symbol[len(snumber) - invp - 1] * int(d)
        for invp, d
        in enumerate(snumber)
        if d != "0"  # There is no zero in the roman number system.
    ])
    for old, new in replacements:
        replaceable = replaceable.replace(old, new)
    return replaceable

if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
