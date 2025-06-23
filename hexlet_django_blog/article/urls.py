from django.urls import path
from hexlet_django_blog.article import views



urlpatterns = [
    path("", views.IndexView.as_view(), name='articles_index'),
    path('create/', views.ArticleCreateView.as_view(), name='articles_create'),
    path('<int:id>/edit/', views.ArticleEditView.as_view(), name='articles_update'),
    path('<int:id>/delete/', views.ArticleDeleteView.as_view(), name='articles_delete'),
    path("<int:id>/", views.ArticleView.as_view(), name='articles_show'),

]
