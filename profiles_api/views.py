from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API Viwe"""
    def get(self, request, format=None):
        """Return a list of APIView features"""

        an_apiview =[
            'Uses HTTP methods as function (get, put, post, patch, delete)',
            'Is similar to a traditional Django View',
            'Gives you the nos control over your application logic',
            'Is mapped manually to URLS'
        ]
        return Response({'message':'hello', 'an_apiview':an_apiview})
