from django.urls import path

from . import views
from .views import HomeView, ArticleView, AddPostView, UpdatePostView, DeletePostView, CategoryView, \
    AddCategoryView, CategoryListView, AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleView.as_view(), name='article'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('like/', views.like),
]
