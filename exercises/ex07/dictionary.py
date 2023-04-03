"""EX07 - Dictionary Functions."""

__author__ = "730489449"


def invert(dict_1: dict[str, str]) -> dict[str, str]: 
    """Given a dictionary of [str, str], invert should return a dict[str, str] that inverts the keys and the values. The keys of the input list becomes the values of the output list and vice versa."""
    result: dict[str, str] = {}

    for key in dict_1: 
        if dict_1[key] in result:
            raise KeyError("Keys must be unique.")
        result[dict_1[key]] = key
    return result


def favorite_color(dict_2: dict[str, str]) -> str:
    """Create a function in your dictionary.py file called favorite_color."""
    colors: dict[str, int] = {}

    for key in dict_2: 
        if dict_2[key] in colors:
            colors[dict_2[key]] += 1
        else: 
            colors[dict_2[key]] = 1
    result = ""
    count = 0 
    for color in colors:
        if result == "": 
            result = color 
            count = colors[color]
        else:
            if colors[color] > count: 
                result = color
                count = colors[color]
    return result


def count(list_1: list[str]) -> dict[str, int]:
    """Given a list[str], this function will produce a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for i in list_1: 
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result 
