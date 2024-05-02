from django import forms
from blog.models import BlogPost

JOBS = (
    ("python", "Développeur Python"),
    ("javascript", "Développeur Javascript"),
    ("C#", "Développeur C#"),
)

# Formulaire classique
class SignUpForm(forms.Form):
    pseudo      = forms.CharField(max_length=8, required=False)
    email       = forms.EmailField()
    password    = forms.CharField(min_length=6, widget=forms.PasswordInput())
    job         = forms.ChoiceField(choices=JOBS)
    cgu_accept  = forms.BooleanField(initial=True)
    
    def clean_pseudo(self):
        pseudo = self.cleaned_data.get("pseudo")
        if "$" in pseudo:
            raise forms.ValidationError("Le pseudo ne peut pas contenir de $")
        return 

# Formulaire lié a un modèle
class BlogPostForm(forms.ModelForm):
    class Meta:
        model   = BlogPost
        #fields  = "__all__"
        #exclude  = ["title", "slug"]
        fields  = ["title",
                   "date",
                   "author",
                   "category",
                   "description"]
        labels  = {"title": "Titre",
                   "category": "Catégorie",
                   "author": "Auteur"}
        widgets = {"date": forms.SelectDateWidget(years=range(1990, 2040))}