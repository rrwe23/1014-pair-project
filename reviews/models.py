from tabnanny import verbose
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Review(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    movie_name = models.CharField(max_length=20)
    grade = models.IntegerField(
        default = 3,
        validators = [MaxValueValidator(5),MinValueValidator(1)],
        verbose_name = "평점",
        
    )

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
