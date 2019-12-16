from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

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

    def post(self, request):
        """Create a Hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST 
            )
        
    def put(self, request, pk=None):
        """Hendle updating an Object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle  a partial update  of an object"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """Delete an Object"""
        return Response({'method': 'DELETE'})


class HelllViewSet(viewsets.ViewSet):
    """Test API View Set"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello Message"""
         
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            "Automatically maps to URLs using Routers",
            "Provides more functionally with less code",
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})


    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
             return Response(
                 serializer.errors,
                 status=status.HTTP_400_BAD_REQUEST
             )

    def retrieve(self, request, pk=None):
        """Handle getting object by it's ID"""
        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """Handle updating an Object"""
        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing object"""
        return Response({'http_method': 'DELETE'})

