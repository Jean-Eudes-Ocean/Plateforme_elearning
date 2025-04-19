from django.contrib import admin
from .models import Niveaux, Matiere, Lesson, Commentaire, Reponse

# Register your models here.

admin.site.register(Niveaux)
admin.site.register(Matiere)
admin.site.register(Lesson)
admin.site.register(Commentaire)
admin.site.register(Reponse)
