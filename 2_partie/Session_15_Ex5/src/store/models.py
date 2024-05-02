from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    wikipedia = models.URLField(blank=True)
    
    @property
    def aff(self):
        return f"{self.firstname} {self.lastname}"
    
    def save(self, *args, **kwargs):      
        if not self.slug:
            self.slug = slugify(f"{self.firstname}-{self.lastname}")        
        super().save(*args, **kwargs)


class Book(models.Model):
    ADVENTURE = "AV"
    THRILLER = "TR"
    FANTASY = "FS"
    ROMANCE = "RM"
    HORROR = "HR"
    SCIENCE_FICTION = "SF"
    LITERATURE = "LT"

    GENRES = [
        (ADVENTURE, "Aventure"),
        (THRILLER, "Thriller"),
        (FANTASY, "Fantastique"),
        (ROMANCE, "Romance"),
        (HORROR, "Horreur"),
        (SCIENCE_FICTION, "Science-fiction"),
        (LITERATURE, "Literature")
    ]

    VH = "VH"
    EZ = "EZ"
    AD = "AD"
    IA = "IA"
    HB = "HB"
    
    AUTHORS = [
                (VH, "Victor Hugo"),
                (EZ, "Emile Zola"),
                (AD, "Alexandre Dumas"),
		        (IA, "Isaac Asimov"),
		        (HB, "Henri Beyle"),
    ]
    
    title = models.CharField(max_length=300, blank=False)
    price = models.FloatField(blank=True)
    summary = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    author_bis = models.CharField(max_length=25, blank=True, choices=AUTHORS)
    category = models.CharField(max_length=25, blank=True, choices=GENRES)
    stock = models.IntegerField(default=0)
    
    @property
    def aff(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):      
        if not self.price:
            self.price = 5        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
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
       
if __name__ == '__main__':
    book = Book.objects.get(pk=1)
    print(book.pk)
    print(book.title)
