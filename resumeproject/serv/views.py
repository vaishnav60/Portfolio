from django.shortcuts import render

# Create your views here.
def accomplish(request):
    context={'accomplish':'active'}
    return render(request,'serv/accomplish.html',context)