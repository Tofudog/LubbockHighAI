from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {'id':1, 'name': "Introduction to Artificial Intelligence"},
    {'id':2, 'name': "Programming in Python"},
    {'id':3, 'name': "Data Science"},
    {'id':4, 'name': "Classification"},
    {'id':5, 'name': "Regression"},
    {'id':6, 'name': "Support Vector Machines"},
    {'id':7, 'name': "Decision Trees"},
]

import random
stuff = {
    'nums': [random.randint(0, i+1) for i in range(3, 10)],
}
cp_concepts = ["Rectangle Geometry", "Simulation", "Graphs", "Complete Search w. Recursion"]

def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):
    room = None
    for i in rooms:
        if (i['id'] == int(pk)):
            room = i

    # if room.name == "Learn C++":
    #     room["Daily_Excercise"] = random.choice(cp_concepts)
    context = {'room': room, 'data': stuff}
    return render(request, 'base/room.html', context)
