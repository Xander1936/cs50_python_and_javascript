import datetime

from django.shortcuts import render

# Create your views here.
def index(request):
    # Save the result in the variable called now
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
        # "newyear": True
    })