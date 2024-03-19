import os
import json
import django
from dateparser import parse
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from kristina.models import Author, Quote, Tag

with open(r"C:\Users\Kristina Cherchataya\PycharmProjects\WEB_10\mysite\utils\authors.json", "r", encoding="utf-8") as file:
    authors = json.load(file)
for author in authors:
    date = parse(author.get("born_date")).strftime("%Y-%m-%d")
    Author.objects.get_or_create(name=author.get("fullname"),
                                 born_date=date,
                                 born_location=author.get("born_location"),
                                 description=author.get("description"))

with open(r"C:\Users\Kristina Cherchataya\PycharmProjects\WEB_10\mysite\utils\quotes.json", "r", encoding="utf-8") as file:
    quotes = json.load(file)
for quote in quotes:
    tags = []
    for tag in quote["tags"]:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    is_quote = bool(len(Quote.objects.filter(quote=quote["quote"])))
    if not is_quote:
        a = Author.objects.get(name=quote["author"])
        q = Quote.objects.create(quote=quote["quote"],author=a)
        for tag in tags:
            q.tags.add(tag)