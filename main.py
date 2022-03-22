# from random import randint
#
#
# class Human:
#     def __init__(self, name, age, sex):
#         self.age = age
#         self.sex = sex
#         self.name = name
#
#     def take_a_queue(self, queue):
#         return Queue.static_add_person(queue, self)
#
#     def dequeue(self, queue):
#         return Queue.static_dequeue(queue)
#
#     def __repr__(self):
#         return f'{self.name}, возраст: {self.age}, пол: {self.sex} '
#
#
# class Queue:
#     def __init__(self):
#         self.list_ = []
#         self.length_list = 0
#
#     @staticmethod
#     def static_add_person(queue, human):
#         return queue.add_item(human)
#
#     @staticmethod
#     def static_dequeue(queue):
#         return queue.remove()
#
#     def remove(self):
#         if self.length_list == 0:
#             raise ValueError('Список пуст!')
#         else:
#             del self.list_[-1]
#             self.length_list -= 1
#
#     def add_item(self, human):
#         self.list_.append(human)
#         self.length_list += 1
#
#     def random_add_queue(self, name, age, sex):
#         if len(self.length_list) == 0:
#             self.length_list.append(name, age, sex)
#             return f"Можете пройти без очереди, {self.name}"
#         else:
#             self.list_.insert(randint(1, len(self.list_)),
#                               Human(name, age, sex))
#
#
# Club = Queue()
#
# Marat = Human("Marat", 18, "male")
# Marat.take_a_queue(Club)
# Linar = Human("Linar", 20, "male")
# Linar.take_a_queue(Club)
# Arina = Human("Arina", 18, "female")
# Arina.take_a_queue(Club)
# Regina = Human("Regina", 18, "female")
# Regina.take_a_queue(Club)
# print(Club.list_)
import re

open_brakets = ["<div>", "<p>", "<h1>"]
chose_brakets = ["<div>", "<p>", "<h1>", "</div>", "</p>", "</h1>"]


def append_brakets(file_new, list_):
    with open(file_new, 'r') as file:
        f = file.read()
        brakets = re.findall(r'<[^>]+>', f)
        for i in brakets:
            if i in chose_brakets:
                list_.append(i)


def check_brakets(check_file):
    stack = []
    list_ = []
    append_brakets(check_file, list_)
    for ch in list_:
        if ch in open_brakets:
            stack.append(ch)
        else:
            ch_char = stack.pop()
            if ch_char == '<div>':
                if ch != '</div>':
                    return False

            if ch_char == '<p>':
                if ch != '</p>':
                    return False

            if ch_char == '<h1>':
                if ch != '</h1>':
                    return False

    if len(stack) == 0:
        return True
    return False


print(check_brakets('index.html'))
