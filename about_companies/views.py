from django.shortcuts import get_object_or_404, render
from .models import Company
from django.http import Http404
from django.db.models import Avg
# Create your views here.

def index(request):
    companies = Company.objects.all().order_by("-year") #-year=descending order, year=ascending
    
    number_companies = companies.count()
    avg_year = int(companies.aggregate(Avg("year"))['year__avg'])
    
    return render(request, 'about_companies/index.html', {
        'companies' : companies,
        'total_number_of_companies' : number_companies,
        'average_year' : avg_year
    })
    
def company_detail(request, slug):
#    try:
#        company = Company.objects.get(slug=slug)
#    except:
#        raise Http404()
    
    company = get_object_or_404(Company, slug=slug)
    
    return render(request, "about_companies/company_detail.html", {
        "name" : company.name,
        "year" : company.year, 
        "symbol" : company.symbol,
        "is_nasdaq" : company.is_nasdaq
    })