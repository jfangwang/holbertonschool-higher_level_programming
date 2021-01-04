#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    output = []
    count = 0


    for a in range(list_length):
        try:
            output.append(my_list_1[count] / my_list_2[count])
        except IndexError:
            output.append(0)
            print("out of range")
        except ZeroDivisionError:
            output.append(0)
            print("division by 0")
        except TypeError:
            output.append(0)
            print("wrong type")
        except:
            print("error unknown")
        finally:
            count += 1
    return output
