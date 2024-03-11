# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def Fibbo_N(n):
    list_fibo=[1,1]
    iteration=2
    while iteration < n:
        list_fibo.append(list_fibo[iteration-1]+list_fibo[iteration-2])
        iteration+=1
    return  list_fibo



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(Fibbo_N(8))

