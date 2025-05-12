from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.http import Http404
from django.conf import settings
from .models import UMLDiagram
from .utils import encode_plantuml

import os


class UMLDiagramListView(ListView):
    model = UMLDiagram
    template_name = 'blueprint/list.html'
    context_object_name = 'diagrams'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        diagram_type = self.request.GET.get('type', '')

        qs = UMLDiagram.objects.all()
        if query:
            qs = qs.filter(title__icontains=query)
        if diagram_type:
            qs = qs.filter(diagram_type=diagram_type)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['diagram_type'] = self.request.GET.get('type', '')
        return context


class UMLDiagramDetailView(DetailView):
    model = UMLDiagram
    template_name = 'blueprint/details.html'
    context_object_name = 'diagram'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['explanation_html'] = self.object.explanation
        return context


class PlantUMLPreviewView(View):
    template_name = 'blueprint/preview.html'

    def get(self, request, file_name):
        file_path = os.path.join(settings.BASE_DIR, 'uml', 'puml', file_name)
        print(f"File path: {file_path}")
        if not os.path.isfile(file_path):
            raise Http404("PUML file not found.")

        with open(file_path, 'r') as f:
            content = f.read()

        encoded = encode_plantuml(content)
        plantuml_url = f"https://www.plantuml.com/plantuml/png/{encoded}"

        return render(request, self.template_name, {
            'plantuml_url': plantuml_url,
            'file_name': file_name,
            'puml_code': content,
        })
