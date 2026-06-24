from django import forms
from django.contrib.auth.models import User

from .models import Document


class UploadForm(forms.Form):
    title = forms.CharField(
        label="Tên tài liệu",
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nhập tên tài liệu",
            }
        ),
    )
    file = forms.FileField(
        label="Tệp tài liệu",
        widget=forms.ClearableFileInput(
            attrs={
                "class": "form-control",
            }
        ),
    )


class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        label="Tên tài khoản",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nhập tên tài khoản",
            }
        ),
        help_text="",
    )
    password = forms.CharField(
        label="Mật khẩu",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nhập mật khẩu",
            }
        ),
    )

    class Meta:
        model = User
        fields = ["username", "password"]


class EditDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ["title"]
        labels = {
            "title": "Tên tài liệu",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nhập tên tài liệu mới",
                }
            ),
        }
