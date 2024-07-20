# views.py

from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import BlogPost
from .serializers import BlogPostHomeSerializer, BlogPostSerializer
from .paginations import MyLimitOffsetPagination

class GetTitleDescriptions(ListAPIView):
    queryset = BlogPost.objects.all().order_by('-created_at')
    serializer_class = BlogPostHomeSerializer
    pagination_class = MyLimitOffsetPagination

    def get_paginated_response(self, data):
        return self.paginator.get_paginated_response(data)

class GetBlogById(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'
