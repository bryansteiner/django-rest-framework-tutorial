from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views_tutorial_1
from snippets import views_tutorial_2
from snippets import views_tutorial_3a
from snippets import views_tutorial_3b
from snippets import views_tutorial_3c
from snippets import views_tutorial_4
from snippets import views_tutorial_5
from snippets import views_tutorial_6
from snippets.views_tutorial_6 import SnippetViewSet, UserViewSet
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

# Tutorial 6a

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retreive',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes = [renderers.StaticHTMLRenderer])
#
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
#
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

# Tutorial 6b

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views_tutorial_6.SnippetViewSet)
router.register(r'users', views_tutorial_6.UserViewSet)

urlpatterns = [
    # The API URLs are now determined automatically by the router.
    path('', include(router.urls)),
]

# urlpatterns = format_suffix_patterns([
#     # path('snippets/', views_tutorial_1.snippet_list),
#     # path('snippets/<int:pk>/', views_tutorial_1.snippet_detail),
#
#     # path('snippets/', views_tutorial_2.snippet_list),
#     # path('snippets/<int:pk>', views_tutorial_2.snippet_list),
#
#     # path('snippets/', views_tutorial_3a.SnippetList.as_view()),
#     # path('snippets/<int:pk>', views_tutorial_3a.SnippetDetail.as_view()),
#
#     # path('snippets/', views_tutorial_3b.SnippetList.as_view()),
#     # path('snippets/<int:pk>', views_tutorial_3b.SnippetDetail.as_view()),
#
#     # path('snippets/', views_tutorial_3c.SnippetList.as_view()),
#     # path('snippets/<int:pk>', views_tutorial_3c.SnippetDetail.as_view()),
#
#     # path('snippets/', views_tutorial_4.SnippetList.as_view()),
#     # path('snippets/<int:pk>', views_tutorial_4.SnippetDetail.as_view()),
#     # path('users/', views_tutorial_4.UserList.as_view()),
#     # path('users/<int:pk>', views_tutorial_4.UserDetail.as_view()),
#
#     # path('', views_tutorial_5.api_root),
#     # path('snippets/', views_tutorial_5.SnippetList.as_view(), name='snippet-list'),
#     # path('snippets/<int:pk>/', views_tutorial_5.SnippetDetail.as_view(), name='snippet-detail'),
#     # path('snippets/<int:pk>/highlight/', views_tutorial_5.SnippetHighlight.as_view(), name='snippet-highlight'),
#     # path('users/', views_tutorial_5.UserList.as_view(), name='user-list'),
#     # path('users/<int:pk>/', views_tutorial_5.UserDetail.as_view(), name='user-detail'),
#
#     # path('', views_tutorial_6.api_root),
#     # path('snippets/', snippet_list, name='snippet-list'),
#     # path('snippets/<int:pk>/', snippet_detail, name='snippet=detail'),
#     # path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     # path('users/', user_list, name='user-list'),
#     # path('users/<int:pk>/', user_detail, name='user-detail')
# ])
