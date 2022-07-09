from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """returns a list APIview features"""
        
        an_apiview=[
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'is similar to a traditional Django view',
            'Gives you the most control over your app',
            'is mapped manually to Urls.'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})