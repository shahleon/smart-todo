from django.urls import path
from . import views

app_name = "todo" 

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:list_id>/', views.listitems, name='list_items'),
    path('templates', views.templates, name='templates'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("password_reset", views.password_reset_request, name="password_reset")
]
