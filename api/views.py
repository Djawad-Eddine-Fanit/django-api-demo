from rest_framework import generics, permissions,filters,status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


from .models import BlogPost ,Category
from .serializers import BlogPostSerializer, RegisterSerializer , CategorySerializer
from .permissions import IsAuthorOrReadOnly ,IsAdminOrReadOnly
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .pagination import DynamicPagination

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content','author__username']
    pagination_class = DynamicPagination
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class MyBlogPostList(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
    pagination_class = DynamicPagination
    def get_queryset(self):
        return BlogPost.objects.filter(author=self.request.user)

class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    lookup_field = 'slug'          # Look this up in the database
    lookup_url_kwarg = 'slug'

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            },
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }, status=status.HTTP_201_CREATED)
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'slug'          # Look this up in the database
    lookup_url_kwarg = 'slug'

