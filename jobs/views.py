from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.core import serializers
from django.urls import resolve

from .models import Job

def index(request):
    # Quick landing page
    latest_job_list = Job.objects.order_by('-submitted_at')[:5]
    context = {
        'latest_job_list': latest_job_list,
        'count': latest_job_list.count()
        }
    return render(request, 'index.html', context)

def batch_jobs(request):
    import json
    dataObj = []

    # Query all results
    q = Job.objects.all()

    # Get URL Parameters
    submitted_after = request.GET.get('filter[submitted_after]')
    submitted_before = request.GET.get('filter[submitted_before]')
    min_nodes = request.GET.get('filter[min_nodes]')
    max_nodes = request.GET.get('filter[max_nodes]')
    
    # If parameter exists, filter query results
    if submitted_after:
            # Having trouble with the URL Encoding. Using replace() as a quick fix
            q = q.filter(submitted_at__gte=submitted_after.replace("'",'').replace(" ",'+')) 

    if submitted_before:
            q = q.filter(submitted_at__lte=submitted_before.replace("'",'').replace(" ",'+'))

    if min_nodes:
            q = q.filter(nodes_used__gte=min_nodes)

    if max_nodes:
            q = q.filter(nodes_used__lte=max_nodes)

    # serialize and prepare data
    q_json = serializers.serialize('json', q, fields = ('batch_number', 'submitted_at', 'nodes_used'))
    data = json.loads(q_json)

    # Create formatted data object based on filtered data
    for job in data:
        dataObj.append({
            "links": {
                "self": request.get_full_path()
            },
            "data": {
                "type": "batch_jobs",
                "id": job['pk'],
                "attributes": job['fields']
            }
        })

    # Prepare data to be returned to the view
    context = {
        "jobs": str(dataObj)
    }
    
    # Return json string to the view
    return render(request, 'batch_jobs.html', context)
