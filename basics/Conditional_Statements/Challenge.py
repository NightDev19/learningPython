"""
Grade Average Program    

Create a program that makes the user input 3 grades and then calculates the average of the grades. 
then check if the grade is:

> 100 or <=50 ~ Invalid Grade
98 - 100 ~ Highest Honor
95 - 97 ~ With High Honors
90 - 94 ~ With Honors
75 - 89 ~  Pass
74 - 51 ~ Failed

"""

G1 = int(input("Enter the first grade: "))
G2 = int(input("Enter the second grade: "))
G3 = int(input("Enter the third grade: "))

ave = (G1 + G2 + G3) / 3

print("The average is: ", str(ave))

if ave > 100 or ave <= 50:
    print("Invalid Grade")
elif ave >= 98 and ave <= 100:
    print("Highest Honor")
elif ave >= 95 and ave <= 97:
    print("With High Honors")
elif ave >= 90 and ave <= 94:
    print("With Honors")
elif ave >= 75 and ave <= 89:
    print("Pass")
else:
    print("Failed")
