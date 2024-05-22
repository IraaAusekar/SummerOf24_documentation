def getNumbers():
    
    num = int(input("how many numbers do you want to generate? "))
    return(num)

def fibonacci(num):
    #x = int(input('how many numbers do you want in your sequence?: '))
    #print("The 1st value of the sequence is 0")
   # print("The 2nd value of the sequence is 1")
    list4 = [0,1]
   
    for y in range(num-2):
        z= (list4[-1] + list4[-2])
        #print("The " + str(y+3) +"th value of the sequence is " + str(z))
        list4.append(z)

    return(list4)

def lucky(num):

    #total = int(input("how many lucky numbers do you want? "))

    upper_limit = num*3

    l = []

    for n in range(1,upper_limit):
        l.append(n)

#alternatively we can also do this
#l = list(range(1,101))

    for n in l:
        if n%2==0:
            l.remove(n)

    for n in l:
        if (n+7)%6==0:
            l.remove(n)
    #print(l)
    #print(len(l))
    return(l)

def generate_sequence():
    
    sequence= input("What type of sequence do you want to generate? If Fibonacci, press 4. If Lucky, press 7. ")
    
#     if sequence!=4 and sequence!=7:
#         sequence= int(input("Number not recognised. please try again."))
    
    #num = getNumbers()
    
    if sequence == '4' or sequence == '04':
        num = getNumbers()
        x = fibonacci(num)
        print('Your Fibonacci numbers have been generated. Please check your variable.')
        return(x)
        
    elif sequence == '7' or sequence == '07':
        num = getNumbers()
        x = lucky(num)
        print('Your Lucky numbers have been generated. Please check your variable.')
        return(x)
        
    else:
        print('Oops! Wrong Input. Please try again')
        generate_sequence()
    
    #return(x)
