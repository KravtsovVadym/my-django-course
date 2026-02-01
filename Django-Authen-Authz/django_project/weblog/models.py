from django.db import models
from django.db.models.functions import Lower

class Tag(models.Model):
    name = models.CharField(verbose_name='Tag', max_length=10, unique=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("name"),  # Overcomes uniqueness through lower()
                name="unique_lower_name_tag")  # Technical identifier
        ]
        ordering  = ['name']  # Sorted (name Tag) alphabetically
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
