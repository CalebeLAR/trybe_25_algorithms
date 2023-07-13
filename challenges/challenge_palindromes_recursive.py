def is_palindrome_recursive(word, low_index, high_index):
    """
    1) pego a posição da primeira e da ultima letra da palavra
    2) se as letras forem iguais e estiverem em posições diferentes eu sigo
    3) subtraio a primeia e a ultima letra da palavra
    4) se o resultado dessa subtração não for uma string vazia eu sigo
    5) repito esse processo até um deles falhar ou a subtração das letras
    resultar uma string vazia

    retira dos extremos, verifica a igualdade e repete
    """
    word = word[low_index:high_index + 1]

    f = len(word) - 1

    if word == "":
        return False

    if (word[0] == word[f]) is False and 0 != f:
        return False

    if word[1:f] == "":
        return True

    return is_palindrome_recursive(word[1:f], 0, f)
