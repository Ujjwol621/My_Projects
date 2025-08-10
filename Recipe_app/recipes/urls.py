
from django.urls import path
from . import views

'app/model_viewtype'
'my_rec/recipe_detail.html'

urlpatterns = [
    path('',views.home, name = "receipe-home"),
    path('recipe/<int:pk>/',views.RecipeDetailView.as_view(), name = "receipe-detail"),
    path('recipe/create/',views.RecipeCreateView.as_view(), name = "receipe-create"),
    path('recipe/<int:pk>/update/',views.RecipeUpdateView.as_view(), name = "receipe-update"),
    path('recipe/<int:pk>/delete/',views.RecipeDeleteView.as_view(), name = "receipe-delete"),
    path('search/', views.recipe_search, name='recipe-search'),
    path('about/',views.about, name = "receipe-about"),
]