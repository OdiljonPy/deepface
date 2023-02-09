import time

import requests
import os

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# import django
# django.setup()


# from app.models import Result


lst_ = os.listdir(path='fake')
print(lst_)
# _lst = os.listdir(path='original')
# print(_lst)
url = 'http://127.0.0.1:8000/test'


# lst = ['2022-12-06_12.02.25.jpg', '20220913_125744_KnwZ7tO.jpg']
# models = ['Facenet', 'VGG-Face']
# metrics = ["cosine", "euclidean", "euclidean_l2"]
def save_response(result):
    with open('fake_original.html', 'r') as file:
        data = file.read()
    data += result
    with open('fake_original.html', 'w') as file:
        file.write(data)


def send_request(img1, img2):
    data = {
        'img1': img1,
        'img2': img2,
        'model': "Facenet512",
        'metric': "cosine"
    }

    response = requests.post(url, data=data)
    return response


if __name__ == '__main__':
    res_lst = []
    idx = 0
    for i in range(len(lst_)):
        for j in range(i + 1, len(lst_)):
            before = time.time()
            res = send_request(lst_[i], lst_[j]).json()
            after = time.time()
            res_lst.append(res)
            idx += 1
            result = f"""<h1>idx: {idx}</h1>
                    <img width="300" src="fake/{lst_[i]}">
                    <img width="300" src="fake/{lst_[j]}">
                    <div class="row align-items-center">
                    <div class="col"><p>model: Facenet512<br>metric: cosine<br>verified: {res.get('verified')}<br>distance: {res.get('distance')}<br>threshold: {res.get('threshold')}<br>time: {after - before}</p></div>
                     """
            save_response(result)

    print(res_lst)
