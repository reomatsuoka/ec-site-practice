from django.shortcuts import render
from django.views.generic import View
from .models import Item
# from django.views.generic import TemplateView
# from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(View):
    # template_name = 'app/index.html'
    # login_url = 'accounts/login'

    def get(self, request, *args, **kwargs):
        item_data = Item.objects.all()
        return render(request, 'app/index.html',{
            'item_data': item_data,
        })

class ItemDetailView(View):
    def get(self, request, *args, **kwargs):
        item_data = Item.objects.get(slug=self.kwargs['sulg'])

        return render(request, 'app/product.html',{
            'item_data': item_data,
        })
