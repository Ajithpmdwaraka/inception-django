from django.shortcuts import render


# Create your views here.
def helloWorld(request):
    moviedata = {
        'movies': [
            {
                "title": "Godfather",
                "year": 1990,
                "summary": "It is a classic mafia film.",
                "success": False,
            },
            {
                "title": "Titanic",
                "year": 2000,
                "summary": "It is a classic mafia film.",
                "success": True,
            },
            {
                "title": "Godfather",
                "year": 1990,
                "summary": "It is a classic mafia film.",
                "success": False,
            },
            {
                "title": "Godfather",
                "year": 1990,
                "summary": "It is a classic mafia film.",
                "success": False,
            },
            {
                "title": "Godfather",
                "year": 1990,
                "summary": "It is a classic mafia film.",
                "success": False,
            },
        ]
    }
    return render(request, "hello.html", moviedata)
