from django.db import models


class UMLDiagram(models.Model):
    DIAGRAM_TYPES = [
        ('class', 'Class Diagram'),
        ('usecase', 'Use Case Diagram'),
    ]

    title = models.CharField(max_length=100)
    diagram_type = models.CharField(max_length=20, choices=DIAGRAM_TYPES)
    image = models.ImageField(upload_to='uml/')
    explanation = models.TextField(blank=True)

    def __str__(self):
        return self.title