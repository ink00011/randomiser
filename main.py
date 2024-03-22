import random
def randomize_list():
    # используем файл names.txt 
    f = open("names.txt", "r")
    # считываем в список строки находящиеся в файле
    list = f.read().splitlines()

    # перемешиваем список содержащий имена
    random.shuffle(list)

    # создаем текстовый файл с названием random_names.txt и открываем его на запись
    f = open("random_names.txt", "w")
    # соединяем элементы списка друг с другом 
    list_as_str = "\n".join(list)
    # записываем результат соединения списка в файл
    f.write(list_as_str)
    # закрываем файл
    f.close()

if __name__ == '__main__':
    randomize_list()
