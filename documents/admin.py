from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "uploaded_by",
        "approved",
        "uploaded_at"
    )

    list_filter = (
        "approved",
    )