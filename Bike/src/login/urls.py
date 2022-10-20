from django.urls import path, include
from login.views import LoginClass, req_logout, RegisterClass, UpdateProfileClass, UserListView, UserDetailView, EditUserClass


urlpatterns = [
  path('login', LoginClass.as_view(), name='login'),
  path('logout', req_logout, name='logout'),
  path('register', RegisterClass.as_view(), name='register'),
  path('update_profile', UpdateProfileClass.as_view(), name='update_profile'),
  path('user-admin', UserListView.as_view(), name='user-admin'),
  path('user-detail-admin/<int:id>', UserDetailView.as_view(), name='user-detail-admin'),
  path('edit-user-admin/<int:id>', EditUserClass.as_view(), name='edit-user-admin')
]
