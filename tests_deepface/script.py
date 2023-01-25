import time

import requests
import os

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# import django
# django.setup()


# from app.models import Result


lst = os.listdir(path='test_images')
print(lst)
print(len(lst))

url = 'http://127.0.0.1:8000/test'
# lst = ['2022-12-06_12.02.25.jpg', '20220913_125744_KnwZ7tO.jpg']
models = ['Facenet', 'VGG-Face']
metrics = ["cosine", "euclidean", "euclidean_l2"]


def send_request(img1, img2, model, metric):
    data = {
        'img1': img1,
        'img2': img2,
        'model': model,
        'metric': metric
    }

    response = requests.post(url, data=data)
    return response


def save_response(result):
    # obj = Result.objects.create(idx=pk, img1=img1, img2=img2, response=str(response.text))
    # obj.save()
    with open('results.html', 'r') as file:
        # file.write(str(response.status_code))
        data = file.read()
    data += result
    with open('results.html', 'w') as file:
        file.write(data)
    # data += f"{response.text}\n{img1}\n{img2}\n"
    # data += '--' * 50
    # data += '\n'
    # data += f"""
    # <div>
    # <h1>{pk}) model: {response.json().get('model')},  metric: {response.json().get('similarity_metric')},  result: {response.json().get('verified')}</h1>
    # <img src="test_images/{img1}" width="640" height="640">
    # <img src="test_images/{img2}" width="640" height="640">
    # <p>
    #     {response.text}
    # </p>
    # </div>
    # """

    # print(response.text, type(response.text))


if __name__ == '__main__':
    pk = 1
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            result = f"""
                    <h1>idx: {pk}</h1>
                    <img width="300" src="test_images/{lst[i]}">
                    <img width="300" src="test_images/{lst[j]}">
                    <div class="row align-items-center">
                    """

            for model in models:
                print(f'model: {model}')
                for metric in metrics:
                    print(f'metric: {metric}')
                    print(f'pk: {pk}\n({lst[i]}, {lst[j]})')
                    before = time.time()
                    res = send_request(img1=lst[i], img2=lst[j], model=model, metric=metric)
                    after = time.time()
                    result += f"""<div class="col">
                        <p>model: {model}<br>metric: {metric}<br>verified: {res.json().get('verified')}<br>distance: {res.json().get('distance')}<br>threshold: {res.json().get('threshold')}<br>time: {after - before}</p>
                    </div>
                    """

            result += """</div>
                        </div>"""
            save_response(result)
            pk += 1
            print()
# print(send_request('2022-12-06_12.02.25.jpg', '20220913_125744_KnwZ7tO.jpg', 'VGG-Face', 'euclidean').text)
