from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserSerializer, UserDeleteSerializer, ChangePasswordSerializer


class UserView(APIView):

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request, pk):
        profile = User.objects.get(pk=pk)
        serializer = UserSerializer(profile)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        if request.user.pk != user.pk:
            return Response({"error": "삭제 권한이 없습니다."}, status=403)
        serializer = UserDeleteSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user.delete()
            return Response({"message": "삭제 완료."}, status=200)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        user_update = User.objects.get(pk=pk)
        serializer = UserSerializer(user_update, data=request.data, partial=True)
        if request.user.pk != user_update.pk:
            return Response({"error": "수정 권한이 없습니다."}, status=403)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = ChangePasswordSerializer(user, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Password updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


















