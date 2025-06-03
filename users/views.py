from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import password_validation

from .serializers import UserRegistrationSerializer
from django.contrib.auth.models import User

@swagger_auto_schema(method='POST', request_body=UserRegistrationSerializer)
@api_view(['POST'])
def user_register_view(request):
    try:
        user = User(username=request.data.get('username'), first_name=request.data.get('first_name'), last_name=request.data.get('last_name'))
        password_validation.validate_password(request.data.get('password'))
        user.set_password(request.data.get('password'))
        user.save()
        return Response({'message':'Success!'})
    except Exception as e:return Response({'Error!':str(e)},  status=403)
