from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views import generic
from django.template import RequestContext
from scheduler.models import Øvedage, Lokaler, Segmenter

# The index page



def index(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    øvedage_list = Øvedage.objects.order_by('-dato')
    context_dict = {'øvedage': øvedage_list}

    # Render the response and send it back!
    return render_to_response('scheduler/index.html', context_dict, context)


