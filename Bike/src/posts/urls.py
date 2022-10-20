from django.urls import path
from posts.views import homepostview, CreatePost, postdetailview, EditPost, adminpostview, DeletePost

urlpatterns = [
    path('postspage/', homepostview, name='postspage'),
    path('post_admin/', adminpostview, name='post_admin'),
    path('post_detail/<slug:slug>', postdetailview, name='post_detail'),
    path('add_post/', CreatePost.as_view(), name='add_post'),
    path('edit/<slug:slug>', EditPost.as_view(), name='update_post'),
    path('delete/<slug:slug>', DeletePost.as_view(), name='delete_post'),
]