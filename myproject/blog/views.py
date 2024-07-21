# views.py

from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import BlogPost , Category
from .serializers import BlogPostHomeSerializer, BlogPostSerializer , CategorySerializer
from .paginations import MyLimitOffsetPagination


class GetTitleDescriptions(ListAPIView):
    serializer_class = BlogPostHomeSerializer
    pagination_class = MyLimitOffsetPagination

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category:
            return BlogPost.objects.filter(categories__id=category)
        return BlogPost.objects.all().order_by('-created_at')
    
class GetBlogById(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'

class GetCategories(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    