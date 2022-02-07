from unicodedata import name
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Company

# Create your views here.
class CompanyView(APIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if(id>0):
            companies = list(Company.objects.filter(id=id).values())
            if len(companies)>0:
                company = companies[0]
                datos = {'message': 'success', 'company': company}
            else:
                datos = {'message': 'Company not found....'}
            return JsonResponse(datos)   
        else:
            companies = list(Company.objects.all().values())
            if len(companies) > 0:
                datos = {'message': 'success', 'companies': companies}
            else: 
                datos = {'message': 'Companies not found....'}
            return JsonResponse(datos)        
    def post(self, request):
        jd = json.loads(request.body)
        Company.objects.create(name=jd['name'],website=jd['website'], foundation= jd['foundation'])
        datos = {'message': 'success'}
        return JsonResponse(datos)   
    def put(self, request, id):
        jd = json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            company = Company.objects.get(id=id)
            company.website= jd['website']
            company.foundation= jd['foundation']
            company.save()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Company not found....'}
        return JsonResponse(datos)  
    def delete(self, request, id):
        companies = list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            Company.objects.filter(id=id).delete()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Company not found....'}
        return JsonResponse(datos)