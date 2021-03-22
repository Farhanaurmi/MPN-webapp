from django.shortcuts import render, redirect, get_object_or_404
from .models import Reviewpost
from .forms import Reviewpostform
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# Create your views here.
def review_post(request):
    form = Reviewpost.objects.all()
    return render(request,'reviewpost/reviewpost.html',  {'form':form})


def creviewpost(request):
    if request.method == 'GET':
        return render(request, 'reviewpost/creviewpost.html', {'form': Reviewpostform()})
    else:
        try:
            dr = Reviewpostform(request.POST)
            new_dr = dr.save(commit=False)
            new_dr.user = request.user
            new_dr.save()
            return redirect('reviewpost')
        except ValueError:
            return render(request, 'reviewpost/creviewpost.html', {'form': Reviewpostform(), 'error':'Error! Try again!'})


@login_required
def dreviewpost(request,m_id):
    dd2 = get_object_or_404(Reviewpost, pk=m_id)
    return render(request,'reviewpost/dreviewpost.html', {'dd':dd2})


@login_required
def mypostd(request,m_id):
    dd2 = get_object_or_404(Reviewpost, pk=m_id, user=request.user)
    return render(request,'reviewpost/mypostd.html', {'dd':dd2})

@login_required
def mypost(request):
    form = Reviewpost.objects.filter(user=request.user, dtime__isnull=True)
    return render(request, 'reviewpost/mypost.html', {'form':form})
    
@login_required
def mypostdelete(request,m_id):
    dd2 = get_object_or_404(Reviewpost, pk=m_id, user=request.user)
    if request.method == 'POST':
        dd2.delete()
        return redirect('mypost')