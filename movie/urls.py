from django.urls import path
from . views import (
    MovieListView, 
    MovieDetailView, 
    MovieCategory, 
    MovieLanguage, 
    MovieSearch, 
    MovieYearArchiveView
)


app_name = "movie"
urlpatterns = [
    path('', MovieListView.as_view(), name = "movie_list"),
    path('<int:pk>/', MovieDetailView.as_view(), name = "movie_detail"),
    path('search/', MovieSearch.as_view(), name = "movie_search"),
    path('category/<str:category>/', MovieCategory.as_view(), name = "movie_category"),
    path('language/<str:language>/', MovieLanguage.as_view(), name = "movie_language"),
    path('year/<int:year>/', MovieYearArchiveView.as_view(), name = "movie_year"),
]
