from django.shortcuts import render
from datetime import datetime

# Create your views here.

curr_tasks = [
    'Create a simple django project',
    'Learn about the various template functions django provides',
    'Learn how to deploy the project'
]

def index_page(request):
    return render(request, 'index.html', context={
        'cur_date': str(datetime.now()),
        'tasks': curr_tasks
    })
