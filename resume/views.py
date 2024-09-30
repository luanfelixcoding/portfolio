from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def projects(request):
    projects_show = [
        {"title": "Example",
         "path": "images/python-logo.png"},
        {"title": "Example2",
         "path": "images/css-logo.png"},
        {"title": "Example3",
         "path": "images/html-logo.png"},
    ]
    return render(request, "projects.html", {"projects_show": projects_show})


def experience(request):
    experiences = [
        {"company": "ABC",
         "position": "python developer"},
        {"company": "ABC2",
         "position": "python developer2"},
        {"company": "ABC3",
         "position": "python developer3"}
    ]
    return render(request, "experience.html", {"experiences": experiences})


def certificate(request):
    return render(request, "certificate.html")
