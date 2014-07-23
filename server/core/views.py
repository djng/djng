# -*- coding: utf-8 -*-
from django.shortcuts import render
import json


def home(request):
    context = {
        'tasks': json.dumps({
            'tasks': [
                'Create new django app',
                'Expose the data over the REST API',
                'Create new ng-controller',
                '...'
            ]
        })
    }

    return render(request, 'index.html', context)
