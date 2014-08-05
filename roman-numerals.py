# I 1 (unus)
# V 5 (quinque)
# X 10 (decem)
# L 50 (quinquaginta)
# C 100 (centum)
# D 500 (quingenti)
# M 1,000 (mille)

symbols = "IVXLCDM  "


def numberToString(digit, one, five, ten):
    return (
        (digit == 9 and (one + ten))
        or (digit > 4 and (five + one * (digit - 5)))
        or (digit == 4 and (one + five))
        or one * digit
    )


def digitAt(number, place):
    # Place is zero-based
    return number % (10 ** (place + 1)) / (10 ** place)


def checkio(number):
    return "".join([
        numberToString(
            digitAt(number, place),
            symbols[place*2],
            symbols[place*2+1],
            symbols[place*2+2]
        )
        for place in range(3, -1, -1)
    ])


if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
