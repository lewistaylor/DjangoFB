'''
Created on Feb 9, 2011

@author: lewis.taylor
'''
from django.conf import settings

def facebook(request):
    facebook_app_url = getattr(settings, 'FACEBOOK_APP_URL', '')
    return { 'FACEBOOK_APP_URL': facebook_app_url }