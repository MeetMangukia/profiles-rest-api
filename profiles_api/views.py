from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """ Return a list of Api views features"""
        an_apiview = [
            'Uses Http method as function (get, post, path, put, delete)',
            'Is similar to a traditional Dajngo View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        # Response must be List, Dictonary
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
        
 