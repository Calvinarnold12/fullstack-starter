from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    """
    View function that renders the Hello World page.
    Demonstrates a simple request/response cycle that can be debugged.
    """
    # import pdb; pdb.set_trace()  Debugger breakpoint - execution pauses here
    
    context = {
        'message': 'Hello World!',
        'title': 'Hello World App',
    }
    return render(request, 'hello/index.html', context)
