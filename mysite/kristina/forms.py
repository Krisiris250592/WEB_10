from django.forms import ModelForm, CharField, TextInput, DateField, ModelChoiceField
from .models import Tag, Author, Quote


class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(ModelForm):
    name = CharField(min_length=2, max_length=100, required=True, widget=TextInput())
    born_date = DateField()
    born_location = CharField(min_length=2, max_length=100, required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ['name', 'born_date', 'born_location']


class QuoteForm(ModelForm):
    quote = CharField(min_length=5, max_length=1000, required=True, widget=TextInput())
    author = ModelChoiceField(queryset=Author.objects.all())

    class Meta:
        model = Quote
        fields = ['quote', 'author']
        exclude = ['tags']
