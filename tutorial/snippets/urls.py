from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views_tutorial_1
from snippets import views_tutorial_2
from snippets import views_tutorial_3a
from snippets import views_tutorial_3b
from snippets import views_tutorial_3c
from snippets import views_tutorial_4
from snippets import views_tutorial_5


urlpatterns = format_suffix_patterns([
    # path('snippets/', views_tutorial_1.snippet_list),
    # path('snippets/<int:pk>/', views_tutorial_1.snippet_detail),

    # path('snippets/', views_tutorial_2.snippet_list),
    # path('snippets/<int:pk>', views_tutorial_2.snippet_list),

    # path('snippets/', views_tutorial_3a.SnippetList.as_view()),
    # path('snippets/<int:pk>', views_tutorial_3a.SnippetDetail.as_view()),

    # path('snippets/', views_tutorial_3b.SnippetList.as_view()),
    # path('snippets/<int:pk>', views_tutorial_3b.SnippetDetail.as_view()),

    # path('snippets/', views_tutorial_3c.SnippetList.as_view()),
    # path('snippets/<int:pk>', views_tutorial_3c.SnippetDetail.as_view()),

    # path('snippets/', views_tutorial_4.SnippetList.as_view()),
    # path('snippets/<int:pk>', views_tutorial_4.SnippetDetail.as_view()),
    # path('users/', views_tutorial_4.UserList.as_view()),
    # path('users/<int:pk>', views_tutorial_4.UserDetail.as_view()),

    path('', views_tutorial_5.api_root),
    path('snippets/', views_tutorial_5.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views_tutorial_5.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', views_tutorial_5.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('users/', views_tutorial_5.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views_tutorial_5.UserDetail.as_view(), name='user-detail'),
])
