from operator import mod
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset()\
                          .filter(status='published')

class Event(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    content = models.TextField()
    date = models.DateField()
    time = models.TimeField(auto_now=False, auto_now_add=False)
    venue = models.CharField(max_length=250)
    announcer = models.CharField(max_length=250)
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
        return reverse('stkevins:event_detail',
                        args=[self.publish.year,
                              self.publish.month,
                              self.publish.day, self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class HomeBanner(models.Model):
    image = models.ImageField(upload_to="banners/", default="/banners/home_bg.jpg")

class ParishPriest(models.Model):
    image = models.ImageField(upload_to="banners/", default="/banners/frjim2.jpeg")
    name = models.CharField(max_length=250)

class AdSlide(models.Model):
    slide = models.ImageField(upload_to="banners/", default="/banners/img1.jpg")

"""
class Sacrament(models.Model):
    name = models.CharField(max_length=41)
    description = models.TextField()
    slug = models.SlugField(max_length=31, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stkevins:sacrament_detail', kwargs={'slug': self.slug})

    class meta:
        ordering = ['name']
        verbose_name_plural = "sacraments"

class Community(models.Model):
    name = models.CharField(max_length=41)
    description = models.TextField()
    slug = models.SlugField(max_length=31, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stkevins:community_detail', kwargs={'slug': self.slug})

    class meta:
        ordering = ['name']
        verbose_name_plural = "communities"

class Society(models.Model):
    name = models.CharField(max_length=41)
    description = models.TextField()
    slug = models.SlugField(max_length=31, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stkevins:society_detail', kwargs={'slug': self.slug})

    class meta:
        ordering = ['name']
        verbose_name_plural = "societies"

class Parishioner(models.Model):
    name = models.CharField(max_length=250)
    id_number = models.CharField(max_length=250, unique=True)
    registration_date = models.DateField()
    societies = models.ManyToManyField(Society, blank=True, related_name='parishoners')
    community = models.ForeignKey(Community, blank=True, on_delete=models.CASCADE, related_name='parishoners')
    sacraments = models.ManyToManyField(Sacrament, blank=True, related_name='parishoners')
    display_pic = models.ImageField(upload_to='banners/', blank=True, null=True, default='/banners/user.png')
    slug = models.SlugField(max_length=31, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stkevins:parishioner_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('stkevins:parishioner_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('stkevins:parishioner_delete', kwargs={'slug': self.slug})

    @property
    def dp_url(self):
        if self.display_pic and hasattr(self.display_pic, 'url'):
            return self.display_pic.url

    class meta:
        ordering = ['name']
        verbose_name_plural = "parishioners"

class Levy(models.Model):
    parishioner = models.ForeignKey(Parishioner, blank=True, on_delete=models.CASCADE, related_name='levies')
    name = models.CharField(max_length=41)
    description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=31, unique=True)

    def __str__(self):
        return self.name + " by " + self.parishioner.name
    
    def get_absolute_url(self):
        return reverse('stkevins:levy_detail',
                        args=[self.publish.year,
                              self.publish.month,
                              self.publish.day, self.slug])

    class meta:
        ordering = ('-publish',)
        verbose_name_plural = "levies"

class Contribution(models.Model):
    parishioner = models.ForeignKey(Parishioner, blank=True, on_delete=models.CASCADE, related_name='contributions')
    name = models.CharField(max_length=41)
    description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=31, unique=True)

    def __str__(self):
        return self.name + " by " + self.parishioner.name

    def get_absolute_url(self):
        return reverse('stkevins:contribution_detail',
                        args=[self.publish.year,
                              self.publish.month,
                              self.publish.day, self.slug])

    class meta:
        ordering = ('-publish',)
        verbose_name_plural = "contributions"

"""