import datetime
from haystack.indexes import *
from haystack import site
from wiki.models import Page

class PageIndex(RealTimeSearchIndex):
    text = CharField(document=True, use_template=True)
    author = CharField(model_attr='author', null=True)
    date = DateTimeField(model_attr='date')

    content_auto = EdgeNgramField(model_attr='content')

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return Page.objects.filter(date__lte=datetime.datetime.now())

site.register(Page, PageIndex)