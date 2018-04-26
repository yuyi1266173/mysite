
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagelist),
    path('article/<int:article_id>/', views.article_page ),
    path('edit/', views.edit_page),
    path('edit/action/', views.edit_action)
]
