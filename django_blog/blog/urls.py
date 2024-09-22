from django.urls import path
from .views import posts_by_tag, register, user_login, user_logout, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
]

from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),  # List all posts
    path('posts/new/', PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View post details
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),  # Edit a post
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Update a post
]

from django.urls import path
from .views import post_detail, comment_edit, comment_delete, search_posts 

urlpatterns = [
     path('search/', search_posts, name='search_posts'),
    path('tags/<str:tag_name>/', posts_by_tag, name='posts_by_tag'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
    path('comments/edit/<int:comment_id>/', comment_edit, name='comment_edit'),
    path('comments/delete/<int:comment_id>/', comment_delete, name='comment_delete'),
]

