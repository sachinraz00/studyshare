from django.urls import path
from .views import home, upload_material

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload_material, name='upload'),
]
