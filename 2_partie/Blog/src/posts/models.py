from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

# On recupere l'utilisateur
User = get_user_model()

# Create your models here.
class BlogPost(models.Model):
    title           = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug            = models.SlugField(max_length=255, unique=True, blank=True)
    author          = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Auteur")
    last_updated    = models.DateTimeField(auto_now=True, verbose_name="Actualisation")
    created_on      = models.DateField(blank=True, null=True, verbose_name="Création")
    published       = models.BooleanField(default=False, verbose_name="Publié")
    content         = models.TextField(blank=True, verbose_name="Contenu")
    
    class Meta:
        ordering        = ['title']
        verbose_name    = "Article"
        
    def __str__(self):
        return self.title
    
    @property
    def author_or_default(self):
        return self.author.username if self.author else "L'auteur inconnu"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)           
        super().save(*args, **kwargs)
    
    