from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from accounts.views import RegisterView, UserDetailView, UserList, UserChangeView, UserPasswordChangeView

app_name = 'accounts'

urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='create'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('user_list/', UserList.as_view(), name='user_list'),
    path('<int:pk>/update/', UserChangeView.as_view(), name="change"),
    path('<int:pk>/password-cange/', UserPasswordChangeView.as_view(), name='password')

]