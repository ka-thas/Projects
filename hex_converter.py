def hex_to_decimal(hex):
    hexdict = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "a": 10,
        "b": 11,
        "c": 12,
        "d": 13,
        "e": 14,
        "f": 15,
    }
    hex = hex[::-1]
    mod = 0
    sum = 0
    for num in hex:
        sum += hexdict[num] * (16**mod)
        mod += 1
    return sum


# TODO
def hex_to_bin(hex):
    hexdict = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "a": 10,
        "b": 11,
        "c": 12,
        "d": 13,
        "e": 14,
        "f": 15,
    }
    hex = hex[::-1]
    mod = 0
    sum = 0
    for num in hex:
        sum += hexdict[num] * 2**mod
        mod += 1
    return


def main():
    print(hex_to_decimal("ff"))
    print(hex_to_bin("ff"))


if __name__ == "__main__":
    main()
