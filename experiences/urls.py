from django.urls import path
from .views import ExperienceListCreateView, ExperienceDetailView

urlpatterns = [
    path('', ExperienceListCreateView.as_view(), name='experience-list-create'),
    path('<int:pk>', ExperienceDetailView.as_view(), name='experience-detail')

]
