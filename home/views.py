from django.shortcuts import render
from django.views.generic import View
from products.models import Product, Category


class HomePageView(View):
    http_method_names = ["get"]
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        context = {
            "categories": Category.objects.all(),
        }
        return render(request, template_name=self.template_name, context=context)
