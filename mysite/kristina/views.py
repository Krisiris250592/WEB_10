from django.shortcuts import render, redirect
from .forms import TagForm, AuthorForm, QuoteForm
from .models import Tag, Author, Quote
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.
def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'kristina/index.html', context={'quotes': quotes_on_page})


@login_required()
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='kristina:main')
        else:
            return render(request, 'kristina/tag.html', {'form': form})

    return render(request, 'kristina/tag.html', {'form': TagForm()})


@login_required()
def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='kristina:main')
        else:
            return render(request, 'kristina/author.html', {'form': form})

    return render(request, 'kristina/author.html', {'form': AuthorForm()})


@login_required()
def quote(request):
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            return redirect(to='kristina:main')
        else:
            return render(request, 'kristina/quote.html', {"tags": tags, 'form': form})

    return render(request, 'kristina/quote.html', {"tags": tags, 'form': QuoteForm()})


def author_info(request, id):
    author = Author.objects.get(pk=id)
    return render(request, 'kristina/author_info.html', context={'author': author})