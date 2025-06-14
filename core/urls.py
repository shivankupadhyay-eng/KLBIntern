from django.urls import path
from .views import GenerateJWTTokenView, private_endpoint

urlpatterns = [
    path("login/",GenerateJWTTokenView.as_view()),
    path('private/',private_endpoint.as_view())
]
