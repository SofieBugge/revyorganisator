"""Handles the logic for all pages on the site."""
import datetime

from datetime import datetime


from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views import generic
from django.template import RequestContext

from scheduler.models import Øvedage, Lokaler, Segmenter


# The index page.

def index(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    øvedage_list = Øvedage.objects.order_by('-dato')
    context_dict = {'øvedage': øvedage_list}

    # Loop through each category returned, and create a URL attribute.
    # This attribute stores an encoded URL (e.g. spaces replaced with underscores).
    for øvedag in øvedage_list:
        øvedag.url = øvedag.dato.strftime("%Y_%m_%d")

    # Render the response and send it back!
    return render_to_response('scheduler/index.html', context_dict, context)

# The page showing the schedule for an Øvedag.

def øvedag(request, øvedag_dato_url):
    # Request our context from the request passed to us.
    context = RequestContext(request)

#    fikset_dato = øvedag_dato_url.replace('_', '-')
    øvedag_dato = datetime.strptime(øvedag_dato_url,"%Y_%m_%d")

    # Contain the date of the øvedag passed by the user.
    context_dict = {'øvedag_dato': øvedag_dato}

    try:
        # Search for an øvedag on the given date. Raise an exception if we cannot.
        øvedag = Øvedage.objects.get(dato=øvedag_dato)

        # Retrieve all of the associated lokaler.
        lokaler = Lokaler.objects.filter(øvedag=øvedag)

        # Add the results list to the context under name lokaler.
        context_dict['lokaler'] = lokaler
        # Add the øvedag object to the context under the name øvedag.
        context_dict['øvedag'] = øvedag
    except Øvedage.DoesNotExist:
        pass

    # Render the response and return it to the client.
    return render_to_response('scheduler/øvedag.html', context_dict, context)
