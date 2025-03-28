def calculator(x, y, op):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return "unknown value"
    
    operations = {
        '+': x + y,
        '-': x - y,
        '*': x * y,
        '/': x / y if y != 0 else "unknown value"
    }
    
    return operations.get(op, "unknown value")