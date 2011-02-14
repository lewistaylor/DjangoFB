'''
Created on Feb 9, 2011

@author: lewis.taylor
'''
from django.http import HttpResponse, HttpResponseRedirect
from fb import parse_signed_request
from django.conf import settings
from fb.models import FbUser


app_url = getattr(settings, 'FACEBOOK_APP_URL', 'http://www.facebook.com')
secret_key = getattr(settings, 'FACEBOOK_SECRET_KEY', '')

class FacebookMiddleware:
    '''
        We want to appropriately deal with Facebook calls by 
        accomplishing the following things:
        
        1. Check that a facebook signed_request parameter exists.
        
        
        user is signed in, if not redirect to
        a provided login page in settings - FACEBOOK_AUTH_URL
        
        2. If they are, replace the user object in request with
        a facebook user.
    '''
    
    
    def process_request(self, request):
        
        signed_request = request.REQUEST.get("signed_request", '')
        
        if signed_request:
            #logger.debug('facebook request')
            try:
                facebook_params = parse_signed_request(signed_request, secret_key)
            except:
                pass
                # TO DEAL WITH
                
            if facebook_params.get("user_id", ''):
                '''
                User has come through facebook and is logged in
                get user model
                '''
                
                request.fb_user, created = FbUser.objects.get_or_create(user_id=facebook_params['user_id'])
               
            else:
                '''
                User has come through facebook but isn't logged in
                '''
                def facebook_return(request):
                    return "<script>top.location.href='%s';</script>" % getattr(settings, 'FACEBOOK_AUTH_URL')
                    
                return HttpResponse(facebook_return(request))
            
            
        else:
            '''
            User has come through main webapp site.
            User mocked facebook details to maintain compatibility
            '''
            if not getattr(settings, 'DEBUG', False):
                return HttpResponseRedirect(app_url)
            
            request.fb_user, created = FbUser.objects.get_or_create(user_id=-1)

            