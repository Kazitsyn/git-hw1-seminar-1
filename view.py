def greeting():
    print('Приветствую тебя, друг!\n')


def menu():
    print('***********************\nТелефонный справочник\n***********************\n\n***Выберите действие***\n\n 1. Поиск\n 2. Добавить запись\n 3. Показать всю телефонную книгу\n 4. Закрыть справочник')


def show_phonebook():
    path = 'file.txt'
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        print(line)
    file.close()