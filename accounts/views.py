from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer







# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import UserSerializer
#
#
# @api_view(["POST"])
# def signup(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)







