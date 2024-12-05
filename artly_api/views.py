from rest_framework.decorators import api_view
from rest_framework.response import Response

# This code was appropriated from the Code Institute's DRF API walkthrough
@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to the Artly Api."
    })