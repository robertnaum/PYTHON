import sympy as sym

x = sym.Symbol('x')
try:
    func = input("Enter the function: ")
    func_expr = sym.sympify(func)
    derivative = sym.Derivative(func_expr, x)
    evaluated_derivative = sym.Derivative(func_expr, x, evaluate=True)
    print(f"Derivative: {derivative}")
    print(f"Evaluated Derivative: {evaluated_derivative}")
except (sym.SympifyError, TypeError, ValueError) as e:
    print(f"Error: {e}")
