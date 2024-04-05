from django.shortcuts import render

# Create your views here.
def index(request):
	context = {"title": "BrainMap"}
	return render(request, "public/index", context)


def about(request):
	context = {"title": "About BrainMap"}
	return render(request, "public/about.html", context)