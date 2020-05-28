from django.urls import path
from snippets import views_old

urlpatterns = [
    path('snippets/', views_old.snippet_list),
    path('snippets/<int:pk>/', views_old.snippet_detail),
]