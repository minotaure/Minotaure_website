from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string

from Minotaure_website import secrets


def main_page(request):
    return render(request, "website/main_page.html")


def team(request):
    return render(request, "website/team.html")


def contact(request):
    if "message_sent" in request.GET:
        thank_you = True

    if request.method == "POST":
        # we have a completed form
        # get back the form data
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        company = request.POST.get("company", "")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # send the mail

        send_mail(
            subject="[Minotaure][Prise de contact] " + subject,
            message="",
            html_message=render_to_string("website/email_template.html", locals()),
            from_email=secrets.DEFAULT_FROM_EMAIL,
            recipient_list=secrets.DEFAULT_TO_EMAILS
        )

        return redirect("/contact/?message_sent=1")

    return render(request, "website/contact.html", locals())

