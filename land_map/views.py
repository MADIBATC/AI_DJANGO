from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def landMap(request):
    return render(request, 'map.html')