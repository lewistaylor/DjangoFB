"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
from unittest import TestCase
from fb import parse_signed_request



SECRET_KEY = 'secret'
SIGNED_REQUEST = 'vlXgu64BQGFSQrY0ZcJBZASMvYvTHu9GQ0YM9rjPSso.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsIjAiOiJwYXlsb2FkIn0'

SECRET_KEY = 'a4a1b34732716b3eb1bdced9d9c3c343'
SIGNED_REQUEST = 'ruzEr3rFPBm7eL4XhR4mciaRJF3-9Hnys42SlvXWu_U.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTI5NzM0MjU5MSwidXNlciI6eyJjb3VudHJ5IjoidXMiLCJsb2NhbGUiOiJlbl9HQiJ9fQ'

class SimpleTest(TestCase):
    
    def test_facebook_signed_request_parsing(self):
        """
        Tests the decoding of facebooks signed request
        
        Should return {"0":"payload"}
        """
        
        params = parse_signed_request(SIGNED_REQUEST, SECRET_KEY)
        
        self.assertEqual(len(params),2)
        self.assertEqual(params["0"], 'payload')


