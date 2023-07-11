from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    # O teste rejeita implementações que invertem a lógica de "par ou ímpar";
    assert encrypt_message("arogauossap", 5) == "agora_passou"

    # O teste rejeita implementações que não aplicam a regra de índice
    # positivo válido;
    assert encrypt_message("0123456789", -1) == "9876543210"

    # O teste rejeita implementações que aplicam ordenação ao invés de inversão
    assert encrypt_message("0123456789", 10) == "9876543210"

    # O teste rejeita implementações que não validam o tipo das entradas;
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("message_valida", "3")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(False, 3)

    # O teste aprova implementações corretas.
    assert encrypt_message("arogauossap", 5) == "agora_passou"
    assert encrypt_message("odnassapaunitnoc", 8) == "continua_passando"
