mark =int(input("put the student mark"))


if mark >=70 and mark<=100:
    grade ="A"
elif mark >=60 and mark<=70:
    grade ="B"
elif mark >=50 and mark<=60:
    grade ="C"
elif mark >=40 and mark<=50:
    grade ="E"
elif mark >=30 and mark<=40:
    grade ="E"
elif mark >=20 and mark<=30:
    grade ="F"
else:grade ="invalid mark"
print("the grade is:", grade)
