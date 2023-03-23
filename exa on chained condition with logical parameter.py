#chained condition with logical operator
time=input("enter time in 24 hrs format (eg. 13 )")
time=int(time)
if(time>=0 and time <=12):
    print("good morning")
    print("breakast time")
elif(time>=13 and time <=16) :
    print("good afternoon")
    print("lunch time")
elif(time>=17 and time <=20 ) :
    print("good evening")
    print("snacks time")
else:
    print ("wrong input")
