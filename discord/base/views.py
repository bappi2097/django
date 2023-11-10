from django.shortcuts import render


rooms = [
    {"id": 1, "name": "Lets learn python!"},
    {"id": 2, "name": "Vscode is very good"},
    {"id": 3, "name": "I don't want to learn"},
]


# Create your views here.
def home(request):
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request):
    return render(request, "base/room.html")
