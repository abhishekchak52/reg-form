from django.shortcuts import render
from .forms import MemberForm
from django.contrib import messages
# Create your views here.
def member_form(request):
    form = MemberForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        messages.success(request,message='Successfully submitted')
    context = { 'form': form, }
    return render(request,'member_form.html',context)

# def member_confirm(request):
