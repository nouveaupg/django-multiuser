from django.http import HttpResponse
from django.template import loader

DEFAULT_TITLE = "Default MultiUser Site"


def default_page(request):
    """

    :type request: Default multiuser homepage
    """
    title = "title"
    menu = "menu"
    template = loader.get_template("multiuser_login_form.html")
    context = {
        "multi_user_main_title": DEFAULT_TITLE,
    }

    return HttpResponse(template.render(context))


def create_user_page(request):
    if request.method == "GET":
        template = loader.get_template("multiuser_create_user_form.html")
        context = {
            "multi_user_main_title": "Create a new user"
        }
        return HttpResponse(template.render(context, request))
    return HttpResponse("Success")


def reset_password_page(request):
    if request.method == "GET":
        template = loader.get_template("multiuser_reset_password_form.html")
        context = {
            "multi_user_main_title": "Reset password"
        }
        return HttpResponse(template.render(context, request))
