from django.db import models
from .helps import SaveImage


class Artist(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField(null=True)
    famous_rating = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]


class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    cover = models.URLField()
    rating = models.FloatField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]


class Songs(models.Model):
    title = models.CharField(max_length=100)
    cover = models.URLField(null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    listened = models.PositiveBigIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]
