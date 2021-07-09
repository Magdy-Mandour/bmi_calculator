weight = int(input('enter your weight in kg: '))
height = float(input('enter your height in Metre: '))
bmi = round(weight / height ** 2)
print('your bmi is ' + (str)(bmi))

def bmi_text(bmi):
   if bmi < 18:
     print('you are under weight')
   elif bmi >= 18 and bmi <= 25:
       print('you are in a good shape')
   elif bmi >= 25 and bmi <= 30:
       print('you are overweight')
   else:
       print('you are obese')
bmi_text(bmi)    