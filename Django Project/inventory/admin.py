from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(Amino, Bcaa, Beta, Caffeine, LC, NewOne, Post, Pre, Protein, Recovery, Test)
class ViewAdmin(ImportExportModelAdmin):
     pass

