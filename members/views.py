from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import MemberForm
from django.contrib import messages
# Create your views here.



def member_form(request):
    form = MemberForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return redirect('member-success')
    context = { 'form': form, }
    return render(request,'member_form.html',context)

def member_success(request):
    return render(request,'success.html')
