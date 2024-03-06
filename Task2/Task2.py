#calculates answer to the function 
def func(x):
    return(4/(1+x**2))

#figures out the ammount of divisions and where the results of values at divisions 
def divisions(n):
    div=1/n
    yvals=[]
    n=n+1
    while n !=0:
        n=n-1
        x=1-(div*n)
        yvals.append(func(x))

    return(yvals,div)

#calculates area undergraph using the Trapezoidal rule
def TrapezoidRule(yvals,div):
    i=0
    a=0
    while i < len(yvals)-1:
        a=a+yvals[i]+ yvals[i+1]
        i=i+1
    Area=a*div/2
    print("Trapezoid ",i, " Area: ", Area)
    return (Area)

#calculates area undergraph using the Simpson rule
def SimpsonRule(yvals,div):
    n=len(yvals)-1
    Sum=0
    for i , val in enumerate(yvals):
        if i in (0,n):
            Sum=Sum+val
        elif i%2 == 0:
            Sum=Sum+2*val
        else:
            Sum=Sum+4*val

    Area=Sum*div/3
    print("Simpson ",i," Area: ",Area)
    return Area

#calculates error relative to pi
def error(Result):
    return abs((1-(Result/3.1415667))*100)


# calls functions for calculations
yvals,div=divisions(4)
Result1=TrapezoidRule(yvals,div)
#print("Error:",error(Result1),"%")

Result2=SimpsonRule(yvals,div)
#print("Error:",error(Result2),"%")

yvals,div=divisions(12)
Result3=TrapezoidRule(yvals,div)
#print("Error:",error(Result3),"%")

#writes result to text file
f=open("Task2Results.txt","w")
f.write(("Method          N      Value of Pi     Error(%)\n"))
f.write("Trapezoidal     4  ")
f.write(str(Result1))
f.write("  ")
f.write(str(error(Result1)))
f.write("\n")
f.write("Simpson         4  ")
f.write(str(Result2))
f.write("  ")
f.write(str(error(Result2)))
f.write("\n")
f.write("Trapezoidal    12  ")
f.write(str(Result3))
f.write(" ")
f.write(str(error(Result3)))
f.write("\n")
f.close()
