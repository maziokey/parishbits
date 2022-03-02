from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset()\
                          .filter(status='published')


class Reflection(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=250, blank=True, null=True,)
    name = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(upload_to='banners/', blank=True, null=True, default='/banners/user.png')
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    slug = models.SlugField(max_length=250, unique_for_date='publish')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cathedral:reflection_detail',
                        args=[self.publish.year,
                              self.publish.month,
                              self.publish.day, self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)