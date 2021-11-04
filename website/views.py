from django.http.response import HttpResponse
from django.shortcuts import render


def main_page(request):
    return render(request, "website/main_page.html")


def team(request):
    return render(request, "website/team.html")
