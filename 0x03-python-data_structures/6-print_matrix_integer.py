def print_matrix_integer(matrix=[[]]):
    test = 0
    for i in matrix:

        for j in i:
            if test == 0:
                print("{}".format(j), end='')
                test = 1
            else:
                print(" {}".format(j), end='')
        print('')
        test = 0
