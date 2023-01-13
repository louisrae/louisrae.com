from django.urls import path

from . import views
from .views import EssayView

urlpatterns = [
    path("", views.essays, name="essays"),
    path("devlog", views.devlog, name="devlog"),
    path("content", views.content, name="content"),
    path("books", views.books, name="books"),
    path("<slug:slug>/", views.EssayView.as_view(), name="post_detail"),
]
