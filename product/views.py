from django.http import JsonResponse


def get_product(request):
    return JsonResponse({'id': 1, 'name': "Ball"}, safe=False)
