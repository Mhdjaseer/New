from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)

urlpatterns = [
    path('admin/',views.AdminList.as_view()),
    path('users/',views.CreateUserView.as_view(), name='create-user'),
     path('user-apps/',views.CreateUserAppView.as_view(), name='create-user-app'),
     path('user-data/',views.UserDataView.as_view()),
     path('user-profile/',views.UserProfileView.as_view()),
     path('app-detial/',views.UserAndroidAppView.as_view()),

     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

     path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

]
