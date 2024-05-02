from django import forms
from store.models import Book

# Formulaire lié a un modèle
class AddBookForm(forms.ModelForm):
    class Meta:
        model   = Book
        fields  = ["title",
                   "author_bis",
                   "category",
                   "price",
                   "summary"]
        labels  = {"title": "Titre",
                   "author_bis": "Auteur",
                   "category": "Catégorie",
                   "price": "Prix",
                   "summary": "Resumé",
                   }