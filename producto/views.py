from typing import Generic
from django.shortcuts import  render, redirect
from django.urls.base import reverse_lazy

from django.views import generic

# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import  Producto
from .forms import  ProductoForm


# Producto---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------

class ProductoView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = "producto/producto_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class ProductoNew(LoginRequiredMixin, generic.CreateView):
    model = Producto
    template_name = "producto/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url =reverse_lazy("producto:producto_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.created_by = self.request.user 
        return super().form_valid(form)

class ProductoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Producto
    template_name = "producto/producto_form.html"
    context_object_name = "obj"
    #print("aqi")
    form_class = ProductoForm
    success_url =reverse_lazy("producto:producto_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.modified_by = self.request.user.id
        return super().form_valid(form)


def producto_inactivar(request, id):
    producto = Producto.objects.filter(pk=id).first()
    contexto = {}
    template_name = "producto/producto_del.html"

    if not producto:
        return redirect("producto:producto_list")

    if request.method == 'GET':
        contexto = {'obj': producto}

    if request.method == 'POST':
        producto.estado = False
        producto.save()
        return redirect("producto:producto_list")

    return render(request, template_name, contexto)
# Extras-------------------------------------------------------------------------------------------------
