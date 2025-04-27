from rest_framework import generics, permissions
from .models import Experience
from .serializers import ExperienceSerializer

# this view is used to list and create experiences for providers
# The provider can only see their own experiences and create new ones
class ExperienceListCreateView(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.IsAuthenticated]

    # This method is called when retrieving a list of experiences
    def get_queryset(self):
        return Experience.objects.all()

    # This method is called when creating a new experience
    def perform_create(self, serializer):
        if self.request.user.role != 'provider':
            raise PermissionError("Only providers can create an experience.")
        serializer.save(provider=self.request.user)

# experience detail view for retrieving a specific experience
class ExperienceDetailView(generics.RetrieveAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.IsAuthenticated]
