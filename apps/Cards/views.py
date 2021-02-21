from django.views.generic import ListView, DetailView, TemplateView

from apps.Cards.models import Card
from apps.Cards.models import Category


class IndexView(TemplateView):
    template_name = 'content/index.html'


class CardListView(ListView):
    model = Card
    template_name = 'content/cards.html'

    def get_queryset(self):
        queryset = Card.objects.all()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {}
        context['object_list'] = Card.objects.all()
        first_categories = Category.objects.filter(parent=None)
        context['categories'] = first_categories
        path = self.request.path.split('/')
        if path[2]:
            try:
                title = Category.objects.get(pk=path[2])
                context['title'] = title.title
                categories = Category.objects.filter(parent__exact=(path[2]))
                if categories:
                    context['podcategories'] = categories
                    categories_list = [path[2], ]
                    for i in categories:
                        categories_list.append(i.pk)
                    cards = Card.objects.filter(category__in=categories_list)
                    context['object_list'] = cards
                else:
                    cards = Card.objects.filter(category=path[2])
                    context['object_list'] = cards
                    category = Category.objects.get(pk=path[2])
                    if category.parent:
                        parent = Category.objects.get(pk=category.parent.pk)
                        categories = Category.objects.filter(parent__exact=parent)
                        context['podcategories'] = categories
            except:
                title = 'Нет такой категории'
                context['title'] = title.title
                context['object_list'] = ''
        return context


class CardDetailView(DetailView):
    model = Card
    template_name = 'content/card_detail.html'
