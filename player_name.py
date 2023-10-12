def is_valid_player_name(player_name):
    return 

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
