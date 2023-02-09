from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Image
from deepface.DeepFace import verify
from app.models import Result


@api_view(['GET', 'POST'])
def verify_view(request):
    if request.method == 'GET':

        data = {
            'status': 'ok'
        }
        return Response(data)

    elif request.method == 'POST':
        print(request.FILES)
        print(request.POST)
        obj = Image.objects.create(img1=request.FILES['img1'], img2=request.FILES['img2'])
        result = verify(str(obj.img1), str(obj.img2), model_name=request.POST.get('model'),
                        distance_metric=request.POST.get('metric'))
        print(result)
        return Response(result, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def liveness_view(request):
    if request.method == 'GET':
        data = {
            'status': 'ok'
        }
        return Response(data)

    elif request.method == 'POST':
        import time
        import torch
        import pandas as pd
        import albumentations as albu
        from iglovikov_helper_functions.utils.image_utils import load_rgb
        from datasouls_antispoof.pre_trained_models import create_model
        from datasouls_antispoof.class_mapping import class_mapping

        model = create_model("tf_efficientnet_b3_ns")
        model.eval()

        transform = albu.Compose([albu.PadIfNeeded(min_height=400, min_width=400),
                                  albu.CenterCrop(height=400, width=400),
                                  albu.Normalize(p=1),
                                  albu.pytorch.ToTensorV2(p=1)], p=1)

        image = load_rgb("")
        before = time.time()
        with torch.no_grad():
            prediction = model(torch.unsqueeze(transform(image=image)['image'], 0)).numpy()[0]
        after = time.time()
        df = pd.DataFrame({"prediction": prediction, "class_name": class_mapping.keys()})
        result = {
            'time': after - before
        }
        return Response(result, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def test_view(request):
    if request.method == 'GET':
        data = {
            'status': 'ok'
        }
        return Response(data)

    elif request.method == 'POST':
        # print(request.FILES)
        print(request.POST)
        img1 = 'tests_deepface/fake/' + request.POST['img1']
        img2 = 'tests_deepface/fake/' + request.POST['img2']
        # obj = Image.objects.create(img1=request.FILES['img1'], img2=request.FILES['img2'])
        try:
            result = verify(img1, img2, model_name=request.POST.get('model'),
                            distance_metric=request.POST.get('metric'))
        except Exception as e:
            print(e)
            result = {"verified": False, "distance": 0, "threshold": 0, "model": request.POST.get('model'),
                      "detector_backend": "opencv", "similarity_metric": request.POST.get('metric')}
        print(result)
        return Response(result, status=status.HTTP_201_CREATED)
