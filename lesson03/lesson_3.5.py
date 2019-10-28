'''
Программа запрашивает у пользователя строку чисел, разделенных
 пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и
снова нажать Enter. Сумма вновь введенных чисел будет добавляться
к уже подсчитанной сумме. Но если вместо числа вводится специальный
символ, выполнение программы завершается. Если специальный символ
введен после нескольких чисел, то вначале нужно добавить сумму этих
чисел к полученной ранее сумме и после этого завершить программу.
'''

mystr_res = 0
tmp = 0
mystr = input("Input numbers. Press Enter for sum. 'Q' for quit ")
while mystr[-1] != 'Q' or mystr[-1] != 'q':
    mystr = mystr.split()
    print(mystr)
    for el in mystr:
        mystr = str(input("Input numbers. Press Enter for sum. 'Q' for quit "))
        print(mystr.split())
        #tmp = ''.join(tmp)
        #print(tmp)
        #mystr_res = mystr_res + int((mystr[el]))
        if mystr[-1] == 'Q' or mystr[-1] == 'q':
            print("the end")
            break
        else:
            tmp = mystr.split()
            mystr_res = mystr_res + int(tmp[el])
            print(tmp[el])



