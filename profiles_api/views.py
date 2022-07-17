from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API view"""
    serializer_class=serializers.HelloSerializer

    def get(self, request, format=None):
        """returns a list APIview features"""
        
        an_apiview=[
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'is similar to a traditional Django view',
            'Gives you the most control over your app',
            'is mapped manually to Urls.'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self, request):
        """create a hello message with our name"""
        serializer=self.serializer_class(data=request.data)
        if (serializer.is_valid()):
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request,pk=None):
        """Method for updating an object"""
        return Response({'method':'PUT'})
    
    def patch(self, request,pk=None):
        """Method for updating specific fields"""
        return Response({'method':'PATCH'})

    def delete(self, request,pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test APi viewset"""
    serializer_class=serializers.HelloSerializer
    def list(self, request):
        """Return hello message"""
        a_viewset=[
            'actions == list,create,retrieve,update,partial_update',
            'automatically maps to URLs using routers',
            'provides more functionality with less code'

        ]
        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self, request):
        """Create a new Hello message"""
        serializer=self.serializer_class(data=request.data)
        if(serializer.is_valid()):
            name=serializer.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request,pk=None):
        """gets an object by ID"""
        return Response({'http_method':'GET'})

    def update(self, request,pk=None):
        """update an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request,pk=None):
        """update part of an object"""
        return Response({'method':'PATCH'})

    def destroy(self, request,pk=None):
        """remove/delete an object"""
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """create and update profiles"""
    serializer_class =serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)