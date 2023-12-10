
from django.http import JsonResponse

def contact_form(request):
    context = {
        'success': True,
        'message':'Contact form sent successfully'
    }
    return JsonResponse(context)
