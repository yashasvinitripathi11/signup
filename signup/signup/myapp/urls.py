from django.urls import path

from . import views

urlpatterns = [
    path("signup",views.signup, name="signup"),
    path("login",views.login, name="login"),
    path("success",views.success, name="success"),
    path("invalid",views.invalid, name="invalid"),
    path("",views.dashboard, name="dashboard"),
    path("notes",views.notes, name="notes"),
    path("edit_note/<int:id>",views.edit_note, name="edit_note"),
    path("delete_note/<int:id>",views.delete_note, name="delete_note")
]

