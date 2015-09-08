﻿"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

YOUR_INFO = {
    'name' : 'Christian McDonald',
    'bio' : 'Online projects and Data editor at the Austin American-Statesman',
    'email' : '', # Leave blank if you'd prefer not to share your email with other conference attendees
    'twitter_username' : 'crit', # No @ symbol, just the handle.
    'github_username' : "critmcdonald", 
    'headshot_url' : '', # Link to your GitHub, Twitter, or Gravatar profile image.
}

def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,
                'year': datetime.now().year,
            })
    )
