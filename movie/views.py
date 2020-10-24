from django.shortcuts import render
from django.views.generic import ListView,DetailView
from . models import Movie, MovieLink
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
        return context


