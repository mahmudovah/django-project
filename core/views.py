from django.http import HttpResponse

def hello(request):
    print("Javob:>>", request.method)
    return HttpResponse("<h1 style='color:blue'>salom dunyo</h1>")
def bye(request):
    return HttpResponse("Bye world")