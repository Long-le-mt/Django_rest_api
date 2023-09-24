from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    # model_data = Product.objects.all().order_by("?").first()
    print(request.data)
    # data = {}
    # if model_data:
    #     # data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
    #     data = ProductSerializer(model_data).data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # lưu xuống db (commit=False) 
        # instance = serializer.save()
        # print(instance)
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)