from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import TemplateView
from .models import Item


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        items = Item.objects.all()
        context = super(HomePageView, self).get_context_data(**kwargs)
        context.update(
            {
                "items": items,
            }
        )
        return context


class ItemPageView(TemplateView):
    template_name = "item.html"

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        item = Item.objects.get(pk=pk)
        context = super(ItemPageView, self).get_context_data(**kwargs)
        context.update(
            {"item": item, "STRIPE_PUBLISHABLE_KEY": settings.STRIPE_PUBLISHABLE_KEY}
        )
        return context
