from django.db import models


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
    category = models.CharField(choices = CATEGORY_CHOICES, max_length=1)
    language = models.CharField(choices = LANGUAGE_CHOICES, max_length=2)
    status = models.CharField(choices = STATUS_CHOICES, max_length=2)
    year_of_production = models.DateField()
    

    def __str__(self):
        return self.title


    # - tags
    # - download links 
    # - watch links
    # - related movies 
    # - Comment 