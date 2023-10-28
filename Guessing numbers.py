import random

def ru_game():
    def func_random():
        while True:
            count = 0
            num_random = random.randint(1, 10)
            print()
            print('Программа загадала число от 1 до 10')
            user_num = str(input('Какое число загадала программа?: '))

            if user_num.isdigit() and int(user_num) == num_random:
                print()
                count += 1
                print(f'Вы угадали и получаете за это бал\nУ вас {count} баллов')
                print()
                question_exit = str(input('Хотите продолжить игру?: ')).lower()

                if question_exit == 'да':
                    continue

                elif question_exit == 'нет':
                    print()
                    print(f'Вы набрали {count} очков за игру')
                    break

                else:
                    print('Некоректный ввод или ошибка программы.\nИгра приостановлена!')
                    break
    
            elif user_num.isdigit() and not(int(user_num) == num_random):
                print()
                print(f'Вы не угадали! Загаданное число: {num_random}\nУ вас {count} баллов')

                print()
                question = str(input('Хотите продолжить игру?: ')).lower()

                if question == 'да':
                    continue

                elif question == 'нет':
                    print(f'Вы набрали {count} очков за игру')
                    break

                else:
                    print('Некоректный ввод или ошибка программы.\nИгра приостановлена!')
                    break

            else:
                print('Некоректный ввод или ошибка программы.\nИгра приостановлена!')
                break

    question1 = str(input("Хотите поиграть в угадайку чисел?: ")).lower()

    if question1 == 'да':
        func_random()

    elif question1 == 'нет':
        print()
        print('Возвращайтесь, как будет желание поиграть в угадайку')

    else:
        print()
        print('Некоректный ввод или ошибка программы.\nИгра приостановлена!')

        question1 = str(input("Хотите поиграть в угадайку чисел?: ")).lower()

    if question1 == 'да':
        func_random()

    elif question1 == 'нет':
        print()
        print('Возвращайтесь, как будет желание поиграть в угадайку')

    else:
        print()
        print('Некоректный ввод или ошибка программы.\nИгра приостановлена!')

def en_game():
    def func_random():
        while True:
            count = 0
            num_random = random.randint(1, 10)
            print()
            print('The program made a number from 1 to 10')
            user_num = str(input('What number did the program make up?: '))

            if user_num.isdigit() and int(user_num) == num_random:
                print()
                count += 1
                print(f'You guessed right and get a ball for it\nYou have {count} points')
                print()
                question_exit = str(input('Do you want to continue the game?: ')).lower()

                if question_exit == 'yes':
                    continue

                elif question_exit == 'no':
                    print()
                    print(f'You scored {count} points for the game')
                    break

                else:
                    print('Incorrect input or program error.\nThe game is suspended!')
                    break
    
            elif user_num.isdigit() and not(int(user_num) == num_random):
                print()
                print(f"You didn't guess! The hidden number: {num_random}\nYou have {count} points")

                print()
                question = str(input('Do you want to continue the game?: ')).lower()

                if question == 'yes':
                    continue

                elif question == 'no':
                    print(f'You scored {count} points for the game')
                    break

                else:
                    print('Incorrect input or program error.\nThe game is suspended!')
                    break

            else:
                print('Incorrect input or program error.\nThe game is suspended!')
                break

    question1 = str(input("Do you want to play a number guessing game?: ")).lower()

    if question1 == 'yes':
        func_random()

    elif question1 == 'no':
        print()
        print('Come back, as there will be a desire to play guessing games')

    else:
        print()
        print('Incorrect input or program error.\nThe game is suspended!')

    
lang = str(input("Choose the language of the game(Выберите язык игры): ")).lower()

if lang == 'русский' or lang == 'russian':
    ru_game()

elif lang == 'английский' or lang == 'english':
    en_game()

else:
    print()
    print("Некорректный ввод! Программа приостановлена\nIncorrect input! The program is suspended")