def is_valid_player_name(player_name):
    try:
        # Проверка, что введено не пустое имя
        if not player_name.strip():
            raise ValueError("Имя не должно быть пустым. Пожалуйста, введите корректное имя.")

        # Проверка, что введено только буквенное имя
        if not player_name.isalpha():
            raise ValueError("Имя должно состоять только из букв. Пожалуйста, введите корректное имя.")

        # Если все проверки пройдены успешно, вернуть True
        return True

    except ValueError as e:
        # Обработка и вывод сообщения об ошибке
        print(f"Ошибка: {e}")
        # Вернуть False, если имя не соответствует критериям
        return False

def test_is_valid_player_name():
    # Тест на правильное имя
    assert is_valid_player_name("John") == True, "Тест не пройден"

    # Тест на пустое имя
    assert is_valid_player_name("") == False, "Тест не пройден"

    # Тест на имя из цифр
    assert is_valid_player_name("123") == False, "Тест не пройден"

    # Тест на имя из букв и цифр
    assert is_valid_player_name("John123") == False, "Тест не пройден"

    # Тест на имя из букв и пробела
    assert is_valid_player_name("John Doe") == False, "Тест не пройден"

    # Тест на имя из букв и символов
    assert is_valid_player_name("John!") == False, "Тест не пройден"

    print("Все тесты пройдены успешно!")

# Запуск тестов
test_is_valid_player_name()
