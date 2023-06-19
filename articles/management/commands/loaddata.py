from django.core.management.base import BaseCommand
import json
from articles.models import Article


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open('articles.json', 'rb') as f:
            data = json.load(f)
            for record in data:
                article = Article(title=record['fields']['title'], text=record['fields']['text'], published_at=record['fields']['published_at'], image=record['fields']['image'])
                article.save()
            return print('done')