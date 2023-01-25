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
def test_view(request):
    if request.method == 'GET':
        data = {
            'status': 'ok'
        }
        return Response(data)

    elif request.method == 'POST':
        print(request.FILES)
        print(request.POST)
        img1 = 'tests_deepface/test_images/' + request.POST['img1']
        img2 = 'tests_deepface/test_images/' + request.POST['img2']
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
