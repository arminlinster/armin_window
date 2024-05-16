#學號21號 張輝昇作業 on 2024/04/23
# import os
# os.system("cls")

###9.	BMI計算
import math
w,h=eval(input("please input your weight(kg) & height(meter):"))
print (f"BMI:{w/(h**2)}")

###8.	溫度轉換
d=int(input("please input the degreee of F:"))
print (f"攝氏溫度 ={((d-32)*5/9):.2f}")

###7.4	圖形面積
import math
print (f"圖形面積:{(math.pi*(5**2))+((10*5)/2)+(5*10):.0f}")

###7.3	長方形面積
print (f"長方形面積:{5*10:.0f}")


###7.2	三角形面積
area=(10*5)/2
print (f"三角形面積:{(10*5)/2:.0f}")
print (f"三角形面積:{area:.0f}")


###7.1	圖形面積
import math
print (f"圓面積:{math.pi*(5**2)}")


###6.	數學函數
import math
x=int(input("please input the value of x:"))
f=((3*x)**3)+(2*x)-1
print (((3*x)**3)+(2*x)-1)
print (f)
print (f"f(x) = 3x^3+2x-1:{f:}")


###5.	存錢筒：
n=input("please input your name:")
d01=int(input("please input the numbers of $1:"))
d05=int(input("please input the numbers of $5:"))
d10=int(input("please input the numbers of $10:"))
d50=int(input("please input the numbers of $50:"))
print (d01+(d05*5)+(d10*10)+(d50*50))


###4.	兩點距離計算：
import math
x1=int(input("please input the data of 1st x:"))
y1=int(input("please input the data of 1st y:"))
x2=int(input("please input the data of 2nd x:"))
y2=int(input("please input the data of 2nd y:"))
a=((x1-x2)**2)+((y1-y2)**2)
b=math.sqrt(a)
print (b)


###3.	平均值計算：
d1=float(input("please input data1:"))
d2=float(input("please input data2:"))
d3=float(input("please input data3:"))
print (f"{(d1+d2+d3)/3:.2f}")

###2.	單位轉換
a=float(input("please input weight(unit:kg):"))
print (f"{a*2.2:.2f}")

###1.	列印練習
x=123
y=123456
z=12
p=12
q=123
r=123456
# print(x,y,z)
# print(p,q,r)
print(f"{x:>8}{y:>8}{z:>8}")
print(f"{p:>8}{q:>8}{r:>8}")


# import math
# r=float(input("please input radius:"))
# area=math.pi*r**2 #area
# perimeter=2*math.pi*r
# print("sArea:"+'%.2f'%(area) +"\nsperimeter:"+ '%.2f'% perimeter)


# r=float(input("please input radius:"))
# area=3.1416*r**2 #area
# perimeter=2*3.1416*r
# print(f"sArea:{area:.2f} \n sperimeter:{perimeter:.2f}")




# a=int(input("please input data:"))
# print (a+3)

# x = 5
# print (x)

# y="John"
# print (x,y)
# print (6+8)
# print (1,2,3)
# print (2 ** 3)
# print ("6+8")