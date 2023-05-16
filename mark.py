mark1=int(input("Enter the mark of paper1"))
mark2=int(input("Enter the mark of paper2"))
mark3=int(input("Enter the mark of paper3"))
mark4=int(input("Enter the mark of paper4"))
totalmarks=mark1+mark2+mark3+mark4
print("totalmarks is",totalmarks)
percentage=totalmarks/320*100
print('the percentage of all 4 papers is', percentage)
average=totalmarks/4
print('the average is',average)
if percentage>=80:
 print("A+")
elif percentage>=70:
 print('A')
elif percentage>=60 and percentage<70:
 print('B')
elif percentage>=50 and percentage<60:
 print('C')
elif percentage>=40 and percentage<50:
 print('D')
elif percentage>=30 and percentage<40:
 print('E')
elif percentage<30:
 print('U') 
          
          
          
