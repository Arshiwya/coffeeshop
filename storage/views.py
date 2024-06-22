from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from .models import Material


class MaterialHomePageView(ListView):
    template_name = 'storage/index.html'
    queryset = Material.objects.all()
    context_object_name = "materials"


class UpdateMaterialView(UpdateView):
    model = Material
    fields = ["name", "amount"]
    template_name = "storage/material-update.html"

    def get_initial(self):
        initial = super().get_initial()
        initial["amount"] = self.object.amount
        return initial

    def get_success_url(self):
        pk = self.object.id
        return f"/storage/update/{pk}"
