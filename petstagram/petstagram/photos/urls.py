from django.urls import path, include

from petstagram.photos.views import photo_add, photo_details, photo_edit, photo_delete

urlpatterns = [
    path('add/', photo_add, name='photo add'),
    path('<int:pk>/', photo_details, name='photo details'),
    path('edit/<int:pk>/', photo_edit, name='photo edit'),
    path('delete/<int:pk>/', photo_delete, name='photo delete')
]
