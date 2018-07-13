from sympy import *
import sys
import io


def  display_simplified_exp():
	old_stdout = sys.stdout # Memorize the default stdout stream
	sys.stdout = buffer = io.StringIO()

	# exp = input('Enter expression to be simplified and factorized in python format \n')
	x , y = symbols('x y')

	exp = Integral(Integral(sqrt(1/x) , x))
	# symbol_string = ''
	# for i in exp: 
	# 	if i in ' 1234567890':
	# 		pass
	# 	else:
	# 		symbol_string += (' ' + i + ' ')

	# print(symbol_string)			
	simplified_exp = simplify(exp)
	# factorized_exp = factor(exp)

	init_printing()
	print(latex(simplified_exp))
	sys.stdout = old_stdout
	whats_printed = buffer.getvalue()
	latex_simplified_exp = whats_printed


	# print('Factorized Expression : ' + latex(factorized_exp))
	# display the simplifued and fatorized  result in the latex format  
	return latex(latex_simplified_exp)

def display_factorized_exp():
	old_stdout = sys.stdout # Memorize the default stdout stream
	sys.stdout = buffer = io.StringIO()

	x , y = symbols('x y')

	exp = Integral(sqrt(1/x) , x)
	factorized_exp = factor(exp)

	init_printing()
	print(latex(factorized_exp))
	sys.stdout = old_stdout
	whats_printed = buffer.getvalue()
	latex_factorized_exp = whats_printed
	return latex(latex_factorized_exp)
	

print(display_factorized_exp())
print(display_simplified_exp())