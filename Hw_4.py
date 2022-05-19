import os
import shutil

import requests

response = requests.get('https://reqres.in/api/users?page=2')
data_ = response.json()['data']
path_ = r"C:\Users\bogda\PycharmProjects\Homeworks\users_data"


def get_img(count):
    return requests.get(data_[count]['avatar'], stream=True)


def get_path(count):
    return str(data_[count]['id'])


def write_users(path, count):
    with open(path + "/user_info.txt", "w") as file:
        file.writelines(f"{str(data_[count]['email'])}, "
                        f"{str(data_[count]['first_name'])} {str(data_[count]['last_name'])}")


def get_avatar(path, img):
    with open(path + '/avatar.png', 'wb') as f:
        shutil.copyfileobj(img.raw, f)


def get_data(need_path):
    for i in range(len(data_)):
        img = get_img(i)
        path = need_path + get_path(i)
        try:
            if not os.path.exists(path):
                os.mkdir(path)
            get_avatar(path, img)
            write_users(path, i)
        except OSError:
            continue


def main():
    get_data(path_)


if __name__ == "__main__":
    main()
