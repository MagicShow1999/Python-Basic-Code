
#1.
def secret_code():
    base = ""
    word = input("Enter anything:")
    for i in word:
        base = base + str(ord(i))+" "
    print(base)


#2

def word_to_number(word):
    if word == 'one':
        return(1)
    elif word == 'two':
        return(2)
    elif word == 'three':
        return(3)
    elif word == 'four':
        return(4)
    elif word == 'five':
        return(5)
    elif word == 'six':
        return(6)
    elif word == 'seven':
        return(7)
    elif word == 'eight':
        return(8)
    elif word == 'nine':
        return(9)
    elif word == 'ten':
        return(10)
    elif word == 'eleven':
        return(11)
    elif word == 'twelve':
        return(12)
    elif word == 'thirteen':
        return(13)
    elif word == 'fourteen':
        return(14)
    elif word == 'fifteen':
        return(15)
    elif word == 'sixteen':
        return(16)
    elif word == 'seventeen':
        return(17)
    elif word == 'eighteen':
        return(18)
    elif word == 'nineteen':
        return(19)
    elif word == 'twenty':
        return(20)
    elif word == 'thirty':
        return(30)
    elif word == 'forty':
        return(40)
    elif word == 'fifty':
        return(50)
    elif word == 'sixty':
        return(60)
    elif word == 'seventy':
        return(70)
    elif word == 'eighty':
        return(80)
    elif word == 'ninety':
        return(90)
    elif word == 'hundred':
        return(100)
    elif word == 'thousand':
        return(1000)
    elif word == 'million':
        return(1000000)
    elif word == 'billion':
        return(1000000000)

    

#to split the description
number = input("Say a number in English:")

list1 = number.split(' ')

#list2 converts English description into numbers
list2= []
for i in list1:

     list2.append(word_to_number(i.lower()))

#list3 deals with numbers less than 1000
list3 = []
hold =0
for i in list2:
    if i <= 999:
        if hold == 0:
            hold = i
           
        elif hold < i:
            hold = hold*i
        elif hold > i:
            hold = hold+i
    else:
        list3.append(hold)
        list3.append(i)
        hold= 0
        
if hold != 0:
    list3.append(hold)
        

#list4 deals with numbers larger than 1000
list4= []
hold = 0
for i in list3:
    
    if i < 1000:
        if hold == 0 :
            hold = i
    else:
        hold = hold*i
        list4.append(hold)
        hold = 0
    

if hold != 0:
    list4.append(hold)


#add all numbers in list4 together
output=0
for i in list4:
    output +=i


print(output)




#3.Extra Credit

def chinese_character_to_arabic_number(character):
    if character == '一':
        ## '\u4e00'
        return(1)
    elif character == '二':
        ## '\u4e8c'
        return(2)
    elif character == '三':
        ## '\u4e09'
        return(3)
    elif character == '四':
        ## '\u56db'
        return(4)
    elif character == '五':
        ## '\u4e94'
        return(5)
    elif character == '六':
        ## '\u516d'
        return(6)
    elif character == '七':
        ## '\u4e03'
        return(7)
    elif character == '八':
        ## '\u516b'
        return(8)
    elif character == '九':
        ## '\u4e5d'
        return(9)
    elif character == '十':
        ## '\u5341'
        return(10)
    elif character == '百':
        ## '\u767e'
        return(100)
    elif character == '千':
        ## '\u5343'
        return(1000)
    elif character == '万':
        ## '\u4e07'
        return(10000)
    elif character == '萬':
        ## '\u842c'
        return(10000)
    elif character == '億':
        ## '\u5104'
        return(100000000)
    elif character == '亿':
        ## '\u4ebf'
        return(100000000)
    elif character == '兆':
        ## '\u5146'
        return(1000000000000)







list2 = list(input("Say a number in Chinese"))

list3 =[]
for i in list2:

     list3.append(chinese_character_to_arabic_number(i))


list4=[]
hold =0
for i in list3:
    if i <= 9999:
        if hold == 0:
            hold = i
           
        elif hold < i:
            hold = hold*i
        elif hold > i:
            list4.append(hold)
            hold = i

    else:
        
        list4.append(hold)
        
        list4.append(i)
        hold= 0
        
if hold != 0:
    list4.append(hold)


list5=[]

hold = 0
for i in list4:
    
    if i <10000:
        if hold == 0 :
            hold = i
        elif hold > i:
            hold = hold+i
            
            
    
    else:
        list5.append(hold)
        list5.append(i)
        hold =0
        
if hold != 0:
    list5.append(hold)

list6=[]

hold=0
for i in list5:
    if i< 10000:
        if hold==0:
            
            hold=i
    else:
        hold= hold*i
        list6.append(hold)
        hold=0
if hold != 0:
    list6.append(hold)


output=0
for i in list6:
    output +=i


print(output)













        
