from django.shortcuts import render
from datetime import datetime

def index(request):
    date = datetime.today()
    print(date)
    print(type(date))
    return render(request, "DocBlog/index.html", context={"prenom": "Victor", "date" : date})