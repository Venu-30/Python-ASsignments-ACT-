def interest(p,t,r):
    I=p*t*r/100
    print("enter the intrest:",I)
def rectangle(length,width):
    area=length*width
    perimeter=2*(length+width)
    print("The area of rectangle is:",area)
    print("The perimeter of recatangle is:",perimeter)
def speed(u,t,a):
    s=u*t+1/2*a*t*2
    print("The speed value is:",s)
def farenheit(c):
    temp=c*(9/5)+32
    print("The temparature is converted to celcius:",temp)
def BMI(w,h):
    bmi=w/h**2
    print("calculate the BMI value:",bmi)
def calc_total_price(p,n,t):
    sub_total=p*n
    tax=sub_total*(t)/100
    total_amount=sub_total+tax
    print("The amount need to be paid:",total_amount)
def EMI(p,r,n):
    monthly_rate=r/(12*100)
    emi=(p*monthly_rate*(1+monthly_rate)**n)/((1+monthly_rate)**n-1)
    print("The emi amount is:",emi)
