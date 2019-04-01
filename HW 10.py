#Q1：

def triangle_num(number):

    if number==1:
        return 1

        
    return(number+triangle_num(number-1))


triangle_num(100)


#Q2:

def answer_a_question():

    question= input("Are we there yet?")

    if question== "yes":

        return True

    return(answer_a_question())





#Q3：



def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        return quick_sort([e for e in l[1:] if e <= l[0]]) + [l[0]] +\
            quick_sort([e for e in l[1:] if e > l[0]])
        
        
        


print(quick_sort([35, 42, 39, 7, 49, 46, 33, 43, 28, 25]))
