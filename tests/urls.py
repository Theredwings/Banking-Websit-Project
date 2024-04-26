from django.urls import path
from tests import views

urlpatterns = [
    path("", views.home, name="home"),
    path("loan/", views.presnoaloan, name="ploan"),
    path("apply/", views.apply, name="apply"),
    path("login/", views.login.as_view(), name="login"),
    path("aboutus/", views.about.as_view(), name="about"),
    path("banktansfer/", views.banktranfer, name="transfer"),
    path("deposit/", views.deposit, name="deposit"),
    path("logout/", views.logout, name="logout"),
    path('edit/',views.edit)
]
