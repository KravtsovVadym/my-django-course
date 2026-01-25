from django.db import models # type: ignore

class Note(models.Model):
    title = models.CharField('Title', max_length=100)
    body = models.TextField('Note')
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'