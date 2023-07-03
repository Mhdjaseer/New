from .serializers import AdminView, UserSerializer, UserAppSerializer,UserDataSerializer,ProfileSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import AndroidApp, UserApp
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response

class AdminList(generics.ListCreateAPIView):
    queryset = AndroidApp.objects.all()
    serializer_class = AdminView
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def create(self, request, *args, **kwargs):
        # Print the data from the request
        print(request.data)

        # Call the superclass's create method to handle the request
        return super().create(request, *args, **kwargs)


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        # Print the data from the request
        print(request.data)

        # Call the superclass's create method to handle the request
        return super().create(request, *args, **kwargs)


class CreateUserAppView(generics.ListCreateAPIView):
    queryset = UserApp.objects.all()
    serializer_class = UserAppSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        # Print the data from the request
        print(request.data)

        # Call the superclass's create method to handle the request
        return super().create(request, *args, **kwargs)
  


class UserDataView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        serializer = UserDataSerializer(request.user)
        return Response(serializer.data)
    
class UserAndroidAppView(generics.ListAPIView):
    queryset=AndroidApp.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=AdminView
    uthentication_classes = [JWTAuthentication]

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)