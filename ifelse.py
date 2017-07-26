if __name__ == '__main__':
    n = 24
    if(n%2 == 1):
        print("Weird")
    if(n%2 ==0):
        if(n <=5):
            print ("Not Weird")
        elif(n>= 6 and n<=20):
            print("Weird")
        else:
            print("Not Weird")