from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.dates import YearArchiveView

from . models import Movie, MovieLink, HomeMovieSlider



class MovieHomeView(ListView):
    model = HomeMovieSlider
    template_name = "movie/home.html"

    def get_context_data(self, **kwargs):
        slider = HomeMovieSlider.objects.all()[0:3]
        context = super(MovieHomeView, self).get_context_data(**kwargs)
        context['slider_movies'] = slider
        context['recently_added'] = Movie.objects.filter(status='RA')
        context['most_watched'] = Movie.objects.filter(status = 'MW')
        context['top_rated'] = Movie.objects.filter(status='TR')
        return context


class MovieListView(ListView):
    model = Movie
    paginate_by = 10
    # template_name = ".html"


class MovieDetailView(DetailView):
    model = Movie

    def get_object(self):
        object = super(MovieDetailView, self).get_object()
        object.views += 1
        object.save()
        return object

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['links'] = MovieLink.objects.filter(movie=self.get_object())
        context['related_movies'] = Movie.objects.filter(category=self.get_object().category).exclude(id=self.get_object().id)[0:6]
        return context


class MovieCategory(ListView):
    model = Movie
    paginate_by = 10

    def get_queryset(self):
        self.category = self.kwargs['category']
        movies = Movie.objects.filter(category = self.category)
        return movies

    def get_context_data(self, **kwargs):
        context = super(MovieCategory, self).get_context_data(**kwargs)
        context['movie_category'] = self.category
        return context


class MovieLanguage(ListView):
    model = Movie
    paginate_by = 10 

    def get_queryset(self):
        self.language = self.kwargs['language']
        movies = Movie.objects.filter(language = self.language)
        return movies

    def get_context_data(self, **kwargs):
        context = super(MovieLanguage, self).get_context_data(**kwargs)
        context['movie_language'] = self.language
        return context
        


class MovieSearch(ListView):
    model = Movie 
    paginate_by = 10
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
            print(object_list)
            print(query)
        else:
            object_list = self.model.objects.none()
        return object_list
    


class MovieYearArchiveView(YearArchiveView):
    queryset = Movie.objects.all()
    date_field = "year_of_production"
    make_object_list = True
    allow_future = True
    template_name = "movie/movie_list.html"

