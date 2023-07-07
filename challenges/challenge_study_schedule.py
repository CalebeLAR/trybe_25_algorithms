def study_schedule(permanence_period, target_time):
    """
    permanence_period: uma lista de tuplas (a, b) onde a >= b com a, b inteiros
    positivos
    target_time: inteiro positivo

    Retorna a quantidade de estudantes presentes em um target_time especifico
    ou Node caso receba um valor invalido

    Um estudante só estava permanente em um dado periodo target_time se:
    1) O target_time é igual ao horário de entrada do estudante
    2) O target_time é igual ao horário de saída do estudante
    3) O target_time é menor que o horário de entrada do estudante e
    maior que o horário de saida do estudante
    """
    number_of_students_in_period = 0

    if not isinstance(target_time, int):
        return None

    for entry, exit in permanence_period:
        are_integers = isinstance(entry, int) and isinstance(exit, int)

        if not are_integers or (exit < entry) or entry < 0 or exit < 0:
            return None

        p1 = (entry == target_time) or (exit == target_time)
        p2 = (entry < target_time) and (exit > target_time)

        if p1 or p2:
            number_of_students_in_period += 1

    return number_of_students_in_period
