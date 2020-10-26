from django.db import models
from django.urls import reverse
from django.utils.text import  slugify
from django.utils import timezone


CATEGORY_CHOICES = (
    ('action','Action'),
    ('comedy','Comedy'),
    ('drama','Drama'),
    ('romance','Romance'),
)

LANGUAGE_CHOICES = (
    ('EN','English'),
    ('DR','Dari'), # which people also called Persian as well.
)

STATUS_CHOICES = (
    ('RA','Recently added'),
    ('MW','Most watched'),
    ('TR','Top rated'),
)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to = "movie")
    views = models.IntegerField(default=0)
    cast = models.CharField(max_length=50) # cast is the group of actor who make up a film or stagee play
    category = models.CharField(choices = CATEGORY_CHOICES, max_length=10)
    language = models.CharField(choices = LANGUAGE_CHOICES, max_length=2)
    status = models.CharField(choices = STATUS_CHOICES, max_length=2)
    year_of_production = models.DateField()
    trailer = models.URLField()
    created = models.DateTimeField(default = timezone.now)
    
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie:movie_detail', kwargs={
            'slug':self.slug
        })
        

LINK_CHOICES = (
    ('D','DOWNLOAD LINK'),
    ('W','WATCH LINK'),
)
class MovieLink(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_link")
    type = models.CharField(choices=LINK_CHOICES, max_length=1)
    link = models.URLField()


    def __str__(self):
        return str(self.movie)


class HomeMovieSlider(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "HomeMovieSlider")


    def __str__(self):
        return self.movie.title