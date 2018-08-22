from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

DEFAULT_TITLE = "Default MultiUser Site"


def default_page(request):
    """

    :type request: Default multiuser homepage
    """
    title = "title"
    menu = "menu"
    template = loader.get_template("multiuser_home_base.html")
    context = {
        "multi_user_main_title": DEFAULT_TITLE,
    }

    return HttpResponse(template.render(context, request))
