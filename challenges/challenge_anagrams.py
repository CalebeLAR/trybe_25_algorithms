map_letters = {
    "a": 0,
    "A": 0,
    "b": 1,
    "B": 1,
    "c": 2,
    "C": 2,
    "d": 3,
    "D": 3,
    "e": 4,
    "E": 4,
    "f": 5,
    "F": 5,
    "g": 6,
    "G": 6,
    "h": 7,
    "H": 7,
    "i": 8,
    "I": 8,
    "j": 9,
    "J": 9,
    "k": 10,
    "K": 10,
    "l": 11,
    "L": 11,
    "m": 12,
    "M": 12,
    "n": 13,
    "N": 13,
    "o": 14,
    "O": 14,
    "p": 15,
    "P": 15,
    "q": 16,
    "Q": 16,
    "r": 17,
    "R": 17,
    "s": 18,
    "S": 18,
    "t": 19,
    "T": 19,
    "u": 20,
    "U": 20,
    "v": 21,
    "V": 21,
    "w": 22,
    "W": 22,
    "x": 23,
    "X": 23,
    "y": 24,
    "Y": 24,
    "z": 25,
    "Z": 25,
}


letters_lowercase_maped = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1


def sort_string(string):
    string_maped = [map_letters[letter] for letter in string]
    merge_sort(string_maped)

    sorted_string = ""
    for number in string_maped:
        sorted_string += letters_lowercase_maped[number]

    return sorted_string


def is_anagram(first_string, second_string):
    """
    Para esse problema podemos usar o algoritimo de ordenação merge sort
    criando por Von Neumann.
    Esse algorítimo, porém ordena listas de numeros, e para aproveita-lo nesse
    problema em questão eu transformo as duas string a qual eu quero ordernar
    em duas listas de numeros, onde cada numero representa a posição de sua
    respectiva letra no alfabeto.
    """
    if first_string == "" or first_string == " ":
        return (
            first_string,
            sort_string(second_string),
            False
        )

    if second_string == "" or second_string == " ":
        return (
            sort_string(first_string),
            second_string,
            False
        )

    sorted_first_string = sort_string(first_string)
    sorted_second_string = sort_string(second_string)

    return (
        sorted_first_string,
        sorted_second_string,
        sorted_first_string == sorted_second_string,
    )
