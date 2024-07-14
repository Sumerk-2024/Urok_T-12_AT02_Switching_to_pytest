import pytest
from main import count_vowels


# Тесты для функции count_vowels
def test_only_vowels():
    """Проверка на строку, содержащую только гласные символы."""
    assert count_vowels("aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ") == 30


def test_no_vowels():
    """Проверка на строку, не содержащую гласных символов."""
    assert count_vowels("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ") == 0


def test_mixed_string():
    """Проверка на строку, содержащую смешанные символы."""
    assert count_vowels("Привет, как дела? Hello, how are you?") == 12


def test_empty_string():
    """Проверка на пустую строку."""
    assert count_vowels("") == 0


def test_upper_and_lower_case():
    """Проверка на строку, содержащую гласные символы в разных регистрах."""
    assert count_vowels("aAаёeEиИЁЁю") == 11


# Запуск всех тестов при запуске файла test.py
if __name__ == "__main__":
    pytest.main()
