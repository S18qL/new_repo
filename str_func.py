def to_up(s: str):
    "get string and return this string in uppercase"
    return s.upper()


def to_up_2(s: str):
    return " ".join([i[0].upper() + i[1:] for i in s.split()])
