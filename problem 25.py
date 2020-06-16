#Main function 
def fib():
    f1 = 1
    f2 = 1
    counter = 2
    #Keeps generating next fib number until its of length 1000 digits, keeping track of which index number
    while len(str(max(f1,f2))) < 1000:
        #Sets the smallest of the 2 to the next fib num
        if(f1<f2):
            f1 = f1+f2
        else:
            f2= f1+f2
        counter += 1
    print(max(f1,f2),counter)
        
