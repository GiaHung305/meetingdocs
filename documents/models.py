from django.db import models
from django.contrib.auth.models import User
from pathlib import Path

class Document(models.Model):

    title = models.CharField(max_length=200)

    file = models.FileField(
        upload_to="documents/"
    )

    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    approved = models.BooleanField(
        default=False
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

    @property
    def file_name(self):
        return Path(self.file.name).name
