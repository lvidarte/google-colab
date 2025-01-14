import pytest
from unittest.mock import patch
from io import StringIO
from adivina_el_numero import adivina_el_numero


def test_adivina_el_numero_correcto():
    user_inputs = ['50']
    with patch('builtins.input', side_effect=user_inputs):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('random.randint', return_value=50):
                adivina_el_numero()
                output = fake_out.getvalue().strip()
                assert "¡Felicidades! Adivinaste el número en 1 intentos." in output


def test_adivina_el_numero_demasiado_bajo():
    user_inputs = ['25', '50']
    with patch('builtins.input', side_effect=user_inputs):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('random.randint', return_value=50):
                adivina_el_numero()
                output = fake_out.getvalue().strip()
                assert "Demasiado bajo. Intenta de nuevo." in output
                assert "¡Felicidades! Adivinaste el número en 2 intentos." in output


def test_adivina_el_numero_demasiado_alto():
    user_inputs = ['75', '50']
    with patch('builtins.input', side_effect=user_inputs):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('random.randint', return_value=50):
                adivina_el_numero()
                output = fake_out.getvalue().strip()
                assert "Demasiado alto. Intenta de nuevo." in output
                assert "¡Felicidades! Adivinaste el número en 2 intentos." in output


if __name__ == "__main__":
    pytest.main()