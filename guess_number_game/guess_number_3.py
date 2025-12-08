import random
import os

def get_user_name():  
    while True:
        name = input("Пожалуйста, введите ваш никнейм (или 'стоп' для завершения): ").strip()
        if name.lower() == 'стоп':
            return None
        if name:
            return name
        print("Никнейм не может быть пустым. Попробуйте снова.")

#запрашивает никнейм пользователя
#возвращает никнейм или None, если пользователь ввел 'стоп'

def choose_difficulty():
    while True:
        level = input("Выберите уровень сложности - 'легкий = 1', 'средний = 2' или 'сложный = 3'(или 'стоп' для завершения): ").strip().lower()
        if level == 'стоп':
            return None
        
        try:
            level = int(level)    
            if level == 1:
                return 1, 50, 10
            elif level == 2:
                return 2, 100, 7
            elif level == 3:
                return 3, 200, 5
            else:
                print("Пожалуйста, выберите корректный уровень сложности (1, 2 или 3).")
        except ValueError:
            print("Пожалуйста, введите число 1, 2, 3 или 'стоп'.")
# спрашиваем уровень сложности у пользователя
# возвращает количество попыток в зависимости от выбранного уровня сложности (max_number, attempts)


def get_secret_number(max_number):
    return random.randint(1, max_number)
# возвращает случайное число от 1 до max_number

def get_user_guess():
    while True:
        guess = input("Введите ваше предположение (или 'стоп' для завершения): ")
        if guess.strip().lower() == 'стоп':
            return None
        try:
            return int(guess)
        except ValueError:
            print("Пожалуйста, введите корректное число или 'стоп'.")

# запрашивает у пользователя число или команду 'стоп'
# возвращает число или None, если пользователь ввел 'стоп'

def play_game():
    user_name = get_user_name()
    if user_name is None:
        print("Игра завершена. Спасибо за участие!")
        return
# если пользователь выбрал 'стоп' при вводе ника, завершаем игру

    result = choose_difficulty()
    if result is None:
        print("Игра завершена. Спасибо за участие!")
        return

# если пользователь выбрал 'стоп' при выборе сложности, завершаем игру
    
    level, max_number, attempts = result

# получаем настройки игры

    secret_number = get_secret_number(max_number)
    print(f"Я загадал число от 1 до {max_number}. Попробуйте угадать его за {attempts} попыток!")

# основная логика игры
# цикл по количеству попыток

    for i in range(attempts):
        guess = get_user_guess()
        if guess is None:
            # соххраняем результат как 'прервано пользователем' с количеством использованных попыток i
            save_result(user_name, level, secret_number, i, "прервано пользователем")
            print("Игра завершена. Спасибо за участие!")
            return

# если пользователь ввел 'стоп', завершаем игру

        if guess < secret_number:
            print(f"Слишком мало! Попробуйте еще раз. Попытка {i+1} из {attempts}")
        elif guess > secret_number:
            print(f"Слишком много! Попробуйте еще раз. Попытка {i+1} из {attempts}")
        else:
            print(f"Поздравляю! Вы угадали число за {i+1} попыток!")
            save_result(user_name, level, secret_number, i+1, "победа")
            break

# если пользователь угадал число, поздравляем и выходим из цикла
# иначе даем подсказку
# продолжаем цикл

    else:
        # этот блок выполнится, если цикл закончился БЕЗ break
        print(f"К сожалению, вы не угадали. Загаданное число было: {secret_number}")
        save_result(user_name, level, secret_number, attempts, "проигрыш")

# сообщаем пользователю загаданное число

def save_result(user_name, level, secret_number, attempts_used, outcome):
    # сохраняет результат игры в файл game_results.txt
    path = os.path.join(os.path.dirname(__file__), "game_results.txt")
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"Игрок: {user_name}, Уровень: {level}, Загаданное число: {secret_number}, Попытки использованы: {attempts_used}, Результат: {outcome}\n")

# сохраняет результат игры в файл game_results.txt
# принимает параметры: никнейм пользователя, уровень сложности, загаданное число, количество использованных попыток и исход игры (выигрыш/проигрыш)



# ======================
#      ГЛАВНЫЙ КОД    
# ======================

# Запуск игры      
if __name__ == "__main__":
    play_game()

