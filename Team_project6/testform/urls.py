from django.urls import path
from testform import views
urlpatterns = [
    path('form/', views.form),
]