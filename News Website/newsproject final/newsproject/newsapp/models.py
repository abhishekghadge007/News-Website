from django.db import models

# Create your models here.
class Article(models.Model):
    news_types = (
    (1, "Politics"),
    (2, "India"),
    (3, "World"),
    (4, "Sports"),
    (5, "Health"),
    (6, "Science & Tech."),
    (7, "Finance"),
    (8, "Education"),
    (9, "Listyle"),
    (10, "Weather"),
    (11, "Entertainment"),
    (12, "Travel"),
    (13, "Crime")
    )

    name = models.CharField(max_length=100, null=True, blank=True)
    short_desc= models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField()
    news_img = models.ImageField(default=None)
    type = models.IntegerField(choices=news_types, default=0)



    def __str__(self):
        return self.type


    @property
    def imageUrl(self):
        try :
            url = self.news_img.url

        except:
            url = ''
        return url

