from django.shortcuts import render
#
from django.views.generic import ListView, FormView
#
from .models import Entry
#
from .forms import EntryForm
#
from django.urls import reverse_lazy
# Create your views here.


class AllEntrysView(ListView):
    template_name = 'entrys/entradas.html'
    context_object_name = 'entradas'
    paginate_by = 2


    def get_queryset(self):
        titulo = self.request.GET.get('titulo')
        categoria = self.request.GET.get('categoria')

        datos = Entry.objects.query_entrys(titulo, categoria)

        #ver todo lo que tiene el request
        #self.request.__dict__

        return datos


class CreateNewEntry(FormView):
    template_name = 'entrys/new_entry.html'
    form_class = EntryForm
    success_url = reverse_lazy('entry_app:list_entrys')


    def form_valid(self, form):
        Entry.objects.create(
            category = form.cleaned_data['category'],
            title = form.cleaned_data['title'],
            resumen = form.cleaned_data['resumen'],
            content = form.cleaned_data['content'],
            imagen = form.cleaned_data['imagen'],
            active = form.cleaned_data['active'],
            in_home = form.cleaned_data['in_home'],
            portada = form.cleaned_data['portada'],
            user = form.cleaned_data['user']
        )

        return super(CreateNewEntry, self).form_valid(form)