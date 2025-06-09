from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('add/', views.add_recipe, name='add_recipe'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('explore/', views.explore, name='explore'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:recipe_id>/rate/', views.rate_recipe, name='rate_recipe'),
    path('recipe/<int:recipe_id>/comment/', views.add_comment, name='add_comment'),
    path('fav/<int:recipe_id>', views.fav, name='fav'),
    path('recipe/<int:recipe_id>/toggle_favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorite_recipes, name='favorites'),
    path('search/', views.search_recipes, name='search_recipes'),
]
