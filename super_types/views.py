from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperTypeserializer
from .models import SuperType


# Create your views here.
@api_view(['GET'])
def super_type_list(request):
    super_type = SuperType.objects.all()

    serializer = SuperTypeserializer(super_type, many=True)

    return Response(serializer.data)


