from django.urls import path
from prodavnica import views


urlpatterns = [
    path('register/', views.Register.as_view()),
    path('login/', views.Login.as_view()),
    path('all-users/', views.UserList.as_view()),
    path('user/<str:username>/', views.UserDetail.as_view()),
    path('telefoni/', views.TelefonList.as_view()),
    path('telefoni/<int:pk>/', views.TelefonDetail.as_view()),
    path('user-tel/', views.UserTelefonList.as_view()),
    path('user-tel/<int:pk>/', views.UserTelefonDetail.as_view()),
    path('telefoni/<str:naziv>/', views.TelefonBy.as_view()),
]


