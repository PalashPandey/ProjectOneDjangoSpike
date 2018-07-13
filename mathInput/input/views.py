from django.shortcuts import render
from .mathInputTest import display_simplified_exp ,  display_factorized_exp
# Create your views here.
def home_page(request):
	simplified_exp =   display_simplified_exp()
	factorized_exp =  display_factorized_exp()
	return render(request, 'home_page.html' ,  {"simplified_exp": simplified_exp , "factorized_exp" : factorized_exp})

