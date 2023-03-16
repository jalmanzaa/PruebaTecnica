def max_sub_matrix(A):
    # Inicializar la variable de suma máxima y la variable de suma actual
    max_sum = -float('inf')
    current_sum = 0

    # Recorrer la matriz y actualizar las variables de suma máxima y actual
    for i in range(len(A)):
        current_sum += A[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0

    # Devolver la suma máxima
    return max_sum

A = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sub_matrix(A))