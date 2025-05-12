from django.urls import path
from .views import UMLDiagramListView, UMLDiagramDetailView, PlantUMLPreviewView

urlpatterns = [
    path('', UMLDiagramListView.as_view(), name='uml_list'),
    path('<int:pk>/', UMLDiagramDetailView.as_view(), name='uml_detail'),
    path('puml/<str:file_name>/', PlantUMLPreviewView.as_view(), name='plantuml_preview'),
]
