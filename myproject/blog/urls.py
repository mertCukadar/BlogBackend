from django.urls import path
from .views import GetBlogById, GetTitleDescriptions

urlpatterns = [
    path('blog/', GetTitleDescriptions.as_view(), name='blog-home'),
    path('blog/<int:pk>/', GetBlogById.as_view(), name='blog-detail'),
]