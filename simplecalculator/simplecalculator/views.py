from django.http import JsonResponse, HttpResponseBadRequest
from calculator.simple import SimpleCalculator

def compute(request, input_str=""):
    """
    Computes the input_str
    :param request: The HTTP request object (given by django)
    :param input_str: string of operator and arguments
    :return: JSON responsse with the result
    """

    if not input_str:
        return JsonResponse({'status': 'false', 'message': "Give an operation, e.g 2+2 or ceil20.01"}, status=400)

    # Give an extra space between the operators (more user friendly)
    operators = ['+', '-', '*', '/', 'fmod' ,'abs', 'fabs', 'ceil']
    for o in operators:
        input_str = input_str.replace(o, ' {} '.format(o))

    c = SimpleCalculator()
    c.run(input_str)

    return JsonResponse({'status': 'success', 'result': c.lcd})
