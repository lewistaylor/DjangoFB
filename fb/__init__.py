import base64
import hmac
import hashlib

try: 
    import json
except ImportError:
    from django.core.serializers.json import simplejson as json

def base64_url_decode(data):
        data = data.encode(u'ascii')
        data += '=' * (4 - (len(data) % 4))
        return base64.urlsafe_b64decode(data)
    
    
def parse_signed_request(signed_request, secret_key):
    
    sig, payload = signed_request.split(u'.', 2)
    signature = base64_url_decode(sig)
    data = json.loads(base64_url_decode(payload))

    if data.get('algorithm', '').upper() != 'HMAC-SHA256':
        # DEBUG
        return None

    expected_signature = hmac.new(secret_key, payload, hashlib.sha256).digest()
    
    if expected_signature != signature:
        # DEBUG: Bad signature
        return None
    
    return data