from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .functions.interpolationFunc import generate_response
from .functions.interpolationFunc import get_pyramid


@csrf_exempt
def interpolation_route(request):

    if request.method == 'POST':

        data = json.loads(request.body)

        x_values = data['xValues']
        y_values = data['yValues']
        to_interpolated_values = data['toInterpolatedValues']

        response_data = {
            "interpolatedData": generate_response(x_values, y_values, to_interpolated_values),
            "piramyd": get_pyramid()
        }

        response_json = json.dumps(response_data)

        return HttpResponse(response_json, content_type='application/json')
