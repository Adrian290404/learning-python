def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
    # Tambien se puede en una linea
    # return 'Even' if number % 2 == 0 else 'Odd'
    
print(even_or_odd(8))
print("\n" + even_or_odd(7))