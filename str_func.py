def to_up(s: str):
    "new description from pycharm"
    return s.upper()


def to_up_2(s: str):
    return " ".join([i[0].upper() + i[1:] for i in s.split()])