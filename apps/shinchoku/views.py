from django.shortcuts import render, redirect

from .models import Shinchoku
from .forms import ShinchokuForm


def index(request):
    form = ShinchokuForm()
    shinchokus = Shinchoku.objects.all().order_by('-created')
    context = {
            'form': form,
            'shinchokus': shinchokus,
            }
    return render(request, 'index.html', context)


def new(request):
    if request.method == 'POST':
        user = request.user
        text = request.POST['text']
        shinchoku = Shinchoku(user=user, text=text)
        shinchoku.save()
        return redirect('shinchoku:index')
