#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    res = []
    while i < list_length:
        try:
            res.append(int(my_list_1[i]) / int(my_list_2[i]))
        except ValueError:
            print("wrong type")
            res.append(0)
        except IndexError:
            print("out of range")
            res.append(0)
        except ZeroDivisionError:
            print("division by 0")
            res.append(0)
        finally:
            i += 1
    return res
