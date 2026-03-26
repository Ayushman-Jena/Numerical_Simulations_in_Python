def basic_operations(a, b):
    return {
        "add": a + b,
        "sub": a - b,
        "mul": a * b,
        "div": a / b if b != 0 else None
    }

print(basic_operations(10, 5))
