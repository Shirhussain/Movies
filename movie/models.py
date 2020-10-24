from django.db import models
from django.urls import reverse


CATEGORY_CHOICES = (
    ('A','Action'),
    ('C','Comedy'),
    ('D','Drama'),
    ('R','Romance'),
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
    description = models.TextField()
    image = models.ImageField(upload_to = "movie")
    views = models.IntegerField(default=0)
    cast = models.CharField(max_length=50) # cast is the group of actor who make up a film or stagee play
    category = models.CharField(choices = CATEGORY_CHOICES, max_length=1)
    language = models.CharField(choices = LANGUAGE_CHOICES, max_length=2)
    status = models.CharField(choices = STATUS_CHOICES, max_length=2)
    year_of_production = models.DateField()
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie:movie_detail', kwargs={
            'pk':self.pk
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



    # - tags
    # - download links 
    # - watch links
    # - related movies 
    # - Comment 