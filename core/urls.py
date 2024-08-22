from django.urls import path
from .views import LoginView, BIView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('bi/', BIView.as_view(), name='bi_page'), 
]
