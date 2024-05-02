from django.contrib import admin
from blog.models import BlogPost

# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "published",
        "author",
        "description",
        "date",
        "word_count",
    )
    
    empty_value_display = "Inconnu"
    
    # Les champs de list_display_links ne peuvent pas etre dans list_editable
    list_editable       = ("author", "published", )
    list_display_links  = ("title", )
    
    search_fields = ("title", "slug", )
    list_filter = ("published", "author", )
    autocomplete_fields = ("author", )
    filter_horizontal = ("category", )
    list_per_page = 10