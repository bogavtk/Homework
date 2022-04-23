import os

import requests

result = requests.get("https://reqres.in/api/users?page=2")
dir_path = r"C:\Users\bogda\PycharmProjects\pythonProject7\users_data"
get_data = result.json()['data']

for i in range(len(get_data)):
    users_id_path = dir_path + str(get_data[i]['id'])
    os.mkdir(users_id_path)
    with open(users_id_path + "/avatar.jpg", 'wb') as image_file:
        image_file.write(b'get_data[i]["avatar"]')
    with open(users_id_path + "/user_info.txt", 'w') as f:
        f.writelines(f"{str(get_data[i]['first_name'])}, "
                     f"{str(get_data[i]['last_name'])},"
                     f"{str(get_data[i]['email'])}")

