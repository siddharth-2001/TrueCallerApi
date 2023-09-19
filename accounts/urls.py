from django.urls import include, path
from rest_framework.authtoken import views

from .views import UserListView, CreateUserView, UserDetailView


urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('create/', CreateUserView.as_view(), name='create-user'),
    path('login/', views.obtain_auth_token),
    path('detail/', UserDetailView.as_view(), name='user-detail')
]