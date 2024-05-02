from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    date = datetime.today()
    return render(request, "blog/index.html", context={"prenom": "Victor", "date" : date})

def article(request, numero_article):
    nb_articles = 3
    num_article = list(range(1,nb_articles+1))
    num_article = [str(i).zfill(2) for i in num_article]
    if numero_article in num_article:
        return render(request, f"blog/article_{numero_article}.html")
    return render(request, "blog/article_not_found.html")