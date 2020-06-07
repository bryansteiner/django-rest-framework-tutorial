from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views_function_based
from snippets import views_class_based
from snippets import views_class_based_mixins
from snippets import views_class_based_generic

# function-based --> class-based -->
urlpatterns = [
    # path('snippets/', views_function_based.snippet_list),
    # path('snippets/<int:pk>', views_function_based.snippet_list),
    # path('snippets/', views_class_based.SnippetList.as_view()),
    # path('snippets/<int:pk>', views_class_based.SnippetDetail.as_view()),
    # path('snippets/', views_class_based_mixins.SnippetList.as_view()),
    # path('snippets/<int:pk>', views_class_based_mixins.SnippetDetail.as_view()),
    path('snippets/', views_class_based_generic.SnippetList.as_view()),
    path('snippets/<int:pk>', views_class_based_generic.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)