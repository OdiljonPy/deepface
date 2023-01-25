import time

before = time.time()
from deepface.DeepFace import verify

after = time.time()
print(f'{after - before}')

files = {
    'img1': 'api/img1.jpg',
    'img2': 'api/img2.jpg',
}
print('go')
models = [
    "VGG-Face",
    "Facenet",
    "Facenet512",
    "OpenFace",
    # "DeepFace",
    # "DeepID",
    "ArcFace",
    # "Dlib",
    "SFace",
]
metrics = ["cosine", "euclidean", "euclidean_l2"]
d = {}
lst = []

for model in models:
    for metric in metrics:
        print('=' * 25 + 'BEGIN::' + model + '-' + metric + 25 * '=')
        before = time.time()
        result = verify(files['img1'], files['img2'], model_name=model, distance_metric=metric)
        print(f"verified: {result.get('verified')}")
        print(f"distance: {result.get('distance')}")
        print(f"threshold: {result.get('threshold')}")
        after = time.time()
        print(f'time: {after - before}')
        print('=' * 25 + 'END::' + model + '-' + metric + 25 * '=')
        if result.get('verified') is True:
            d[f'{model}-{metric}'] = after - before
            lst.append((f'{model}-{metric}', after - before))

print('\n\n')
lst.sort(key=lambda x: x[1])
for (i, j) in lst:
    print(i + '::', j)
