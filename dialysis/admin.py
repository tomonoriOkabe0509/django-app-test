from django.contrib import admin
from .models import DialysisRecord

class DialysisRecordAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "patient_id",
        "name",
        "uf",
        "rate"
    )

admin.site.register(DialysisRecord, DialysisRecordAdmin)