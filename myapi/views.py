import json

from django.http.response import JsonResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.response import Response

from .Lib import utils


@api_view(['POST'])
@renderer_classes((XMLRenderer, ))
def get_address_details(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        address = params.get("address", "").replace(" ", "+")
        output_format = params.get("output_format", "")
        response = utils.get_address_details(address)

        if output_format == "json":
            return JsonResponse(response, content_type="application/json")
        elif output_format == "xml":
            return Response(response, content_type="application/xml")
        else:
            raise Exception("Invalid Output Format")

