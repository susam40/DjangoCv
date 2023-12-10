from django.shortcuts import render
from django.http import JsonResponse


def contact_form(request):
    context = {
        'success': True,
        'message':'Contact form sent successfully'
    }
    return JsonResponse(context)

def contact(request):
    return render(request,'contact.html')
