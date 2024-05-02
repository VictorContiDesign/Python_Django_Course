from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
class Author(User):
    prenom  = models.CharField(max_length=50)
    nom     = models.CharField(max_length=50)
    slug    = models.SlugField()
    wiki_url    = models.URLField(blank=True, default="")
    
    @property
    def aff(self):
        return f"{self.prenom} {self.nom}"
    
    def save(self, *args, **kwargs):      
        if not self.slug:
            self.slug = slugify(f"{self.prenom}-{self.nom}")        
        super().save(*args, **kwargs)

    
class Category(models.Model):
    name    = models.CharField(max_length=50)
    slug    = models.SlugField()
    
    @property
    def aff(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):      
        if not self.slug:
            self.slug = slugify(self.name)        
        super().save(*args, **kwargs)  

    
class Book(models.Model):
    title       = models.CharField(max_length=100)
    slug        = models.SlugField()
    category    = models.ManyToManyField(Category)
    price       = models.FloatField(blank=True, default=0)
    summary     = models.TextField(blank=True)
    author      = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    stock       = models.IntegerField(default=0, blank=True)
    
    @property
    def aff(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):      
        if not self.slug:
            self.slug = slugify(self.title)        
        super().save(*args, **kwargs)