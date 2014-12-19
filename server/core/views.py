# -*- coding: utf-8 -*-
import json

from django.shortcuts import render


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
