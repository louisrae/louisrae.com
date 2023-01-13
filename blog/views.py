from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views import generic

from .models import BookList, Devlog, EssayPost

# Create your views here.


def essays(request):
    posts = EssayPost.objects.order_by("-create_date")
    template = loader.get_template("essays.html")
    context = {
        "post_list": posts,
    }
    return HttpResponse(template.render(context, request))


def devlog(request):

    posts = Devlog.objects.all()
    template = loader.get_template("devlog.html")
    context = {
        "devlogs": posts,
    }
    return HttpResponse(template.render(context, request))


def content(request):
    return render(request, "content.html")


def books(request):

    books = BookList.objects.all()
    template = loader.get_template("books.html")
    context = {
        "book_list": books,
    }
    return HttpResponse(template.render(context, request))


class EssayView(generic.DetailView):
    model = EssayPost
    template_name = "content.html"
