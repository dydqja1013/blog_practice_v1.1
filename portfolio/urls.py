from django.urls import path
from . import views

urlpatterns = [
    path('portflio',views.portfolio, name='portfolio'),
]