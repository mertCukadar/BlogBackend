from django.urls import path
from .views import GetBlogById, GetTitleDescriptions , GetCategories

urlpatterns = [
    path('blog/', GetTitleDescriptions.as_view(), name='blog-home'),
    path('blog/<int:pk>/', GetBlogById.as_view(), name='blog-detail'),
    path('categories/', GetCategories.as_view(), name='categories'),
]