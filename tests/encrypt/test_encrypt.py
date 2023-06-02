import pytest
from challenges.challenge_encrypt_message import encrypt_message

invalid_message = 12345


def test_encrypt_message():
    "to success with a odd key"
    assert encrypt_message("message", 3) == "sem_egas"

    "to success with a pair key"
    assert encrypt_message("message", 4) == "ega_ssem"

    "if a exception raised with invalid parameters"
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(invalid_message, 4)

    "if a exception raised with invalid parameters"
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("message", "invalid_key")

    "if return inverted message with a invalid key"
    assert encrypt_message("message", 10) == 'egassem'
