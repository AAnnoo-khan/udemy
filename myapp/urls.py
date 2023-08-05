from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/pdf/', views.post_to_pdf, name='post_to_pdf'),
]
