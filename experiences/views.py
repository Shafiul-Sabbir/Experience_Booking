from rest_framework import generics, permissions
from .models import Experience
from .serializers import ExperienceSerializer

class ExperienceListCreateView(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Experience.objects.all()

    def perform_create(self, serializer):
        if self.request.user.role != 'provider':
            raise PermissionError("Only providers can create an experience.")
        serializer.save(provider=self.request.user)

class ExperienceDetailView(generics.RetrieveAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.IsAuthenticated]
