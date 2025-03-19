import math

def new_avg(arr, newavg):
    summation = 0

    for i in arr:
        summation += i
    
    result = newavg * (len(arr) + 1) - summation

    if result <= 0:
        raise ValueError("La nueva donación esperada debe ser mayor que 0")
    
    return math.ceil(result)

    # Tambien se puede hacer en menos lineas
    
    # result = math.ceil(newavg * (len(arr) + 1) - sum(arr))
    # assert result > 0
    # return result

print(new_avg([2, 2, 4], 3))