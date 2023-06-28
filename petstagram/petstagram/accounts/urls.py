from django.urls import path, include

from petstagram.accounts.views import profile_register, profile_login, profile_details, profile_edit, profile_delete

urlpatterns = [
    path('register/', profile_register, name='profile register'),
    path('login/', profile_login, name='profile login'),
    path('profile/<int:pk>/', include([
        path('', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ]))
]
