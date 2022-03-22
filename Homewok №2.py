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
    append_brakets(check_file,list_)
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
