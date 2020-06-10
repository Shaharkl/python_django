from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
   # return HttpResponse("<h1>Hello World</h1>") # str of HTML code
    return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):
   my_context = {
       "my_text": "This way U can reach me",
       "my_number": 123,
       "my_list": [1, 2, 3, 4, 5, 6]
   }
   return render(request, 'contact.html', my_context)