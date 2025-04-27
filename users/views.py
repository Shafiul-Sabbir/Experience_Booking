from rest_framework import generics
from .serializers import RegisterSerializer
from .models import User

# this view is used to handle user registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

