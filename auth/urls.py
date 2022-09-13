from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

from bunguo.base_view import create_view_paths
from user import views

urlpatterns = [
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.register, name='register'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('revoke-token/', TokenBlacklistView.as_view(), name='token_revoke'),
    path('currentuser/', views.current_user, name='current_user'),
    path('changeloggeduser/', views.change_logged_user),
    path('getotploginurl/', views.get_otp_login_url, {'role_perm': {'content': 'public'}}),
    path('check-otp/', views.check_otp, {'role_perm': {'content': 'public'}}),
    path('send-otp-again/', views.send_otp, {'role_perm': {'content': 'public'}}),
    path('sendresetpasswordlink/', views.send_reset_link, {'role_perm': {'content': 'public'}}),
    path('checktoken/', views.check_token, {'role_perm': {'content': 'public'}}),
    path('setpasswordwithtoken/', views.set_password_with_token, {'role_perm': {'content': 'public'}}),
    path('set_password/', views.set_password, {'role_perm': {'content': 'public'}}),
    path('set_user_password/', views.set_user_password),
    *create_view_paths('user', views.UserViewSet),
    *create_view_paths('customer', views.CustomerViewSet),
    *create_view_paths('contractor', views.ContractorViewSet),
    *create_view_paths('parameter', views.ParameterViewSet),
    *create_view_paths('parametergroup', views.ParameterGroupViewSet),
]
