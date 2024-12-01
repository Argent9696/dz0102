questions_list = [
    ("Какая версия языка сейчас актуальна?", "python3"),
    ("Какая кодировка используется в строках?", "utf8"),
    ("Сколько значений есть у bool?", "2"),
    ("Какой метод используется для чтения ввода пользователя?", "input"),
    ("Что возвращает функция len()?", "длину"),
    ("Какое ключевое слово используется для объявления функции?", "def"),
    ("Какой тип данных представляет целые числа?", "int"),
    ("Какой символ используется для комментариев в Python?", "#"),
    ("Какой модуль используется для работы с математическими функциями?", "math"),
    ("Какой метод преобразует строку в верхний регистр?", "upper"),
]

correct_answers = 0
question_count = 0

for question, correct_answer in questions_list:
    user_answer = input(f'Введите ответ на вопрос: {question} ')
    question_count += 1

    if user_answer.lower() == correct_answer.lower():
        correct_answers += 1
        print("Ok")
    else:
        print("Not correct")

print(f'Пыточная подошла к концу, вы ответили правильно на {correct_answers} из {question_count}.')
