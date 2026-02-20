from django.http import HttpResponse

def index(request):
    print("Index Request is: ", request)
    return HttpResponse("Hello, from index.")
    