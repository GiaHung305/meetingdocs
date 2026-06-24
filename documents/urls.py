from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [

    path(
        "",
        views.home
    ),

    path(
        "upload/",
        views.upload_document
    ),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html"
        )
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view()
    ),

    path(
        "register/",
        views.register
    ),
    
    path(
    "my-documents/",
    views.my_documents
    ),

    path(
        "documents/<int:id>/",
        views.document_detail
    ),

    path(
        "delete/<int:id>/",
        views.delete_document
    ),

    path(
        "edit/<int:id>/",
        views.edit_document
    ),
    path(
        "dashboard/",
        views.dashboard
    ),

    path(
        "approve/<int:id>/",
        views.approve_document
    ),

    path(
        "admin-delete/<int:id>/",
        views.admin_delete_document
    ),
]
