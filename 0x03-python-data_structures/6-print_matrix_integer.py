def print_matrix_integer(matrix=[[]]):
    
    for i in matrix:
        l = 0
        for j in i:
            if l == 0:
                print("{}".format(j), end='')
            else:
                print(" {}".format(j), end='')
            l += 1
        print('')