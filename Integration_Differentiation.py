# Import required library
import sympy as sp

# Define the variable
x = sp.symbols('x')

# Define a function
f = x**3 + 2*x**2 + 3*x + 1

print("Function f(x):", f)

# -------------------------------
# Differentiation
# -------------------------------
df = sp.diff(f, x)

print("\nDerivative of f(x):")
print("df/dx =", df)

# -------------------------------
# Integration
# -------------------------------
integral = sp.integrate(f, x)

print("\nIndefinite Integral of f(x):")
print("∫f(x) dx =", integral)

# -------------------------------
# Definite Integration
# -------------------------------
def_integral = sp.integrate(f, (x, 0, 2))

print("\nDefinite Integral of f(x) from 0 to 2:")
print("∫₀² f(x) dx =", def_integral)