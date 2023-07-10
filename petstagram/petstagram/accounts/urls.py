from django.urls import path, include

from petstagram.accounts.views import profile_details, profile_edit, profile_delete, UserRegisterView, UserLoginView, UserLogoutView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='profile register'),
    path('login/', UserLoginView.as_view(), name='profile login'),
    path('logout/', UserLogoutView.as_view(), name='profile logout'),
    path('profile/<int:pk>/', include([
        path('', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ]))
]
