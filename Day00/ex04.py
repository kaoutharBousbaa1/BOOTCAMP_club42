try:
  num1 = int(input('Type a integer number please: '))
  num2 = int(input('Type another one: (must be an integer)'))
  addition = num1 + num2
  difference = num1 - num2
  product = num1 * num2
  division = num1 / num2
  modulus = num1 % num2
  print('Sum of ',num1 ,'and' ,num2 ,'is :',addition, end = '\n')
  print('Difference of ',num1 ,'and' ,num2 ,'is :',difference, end = '\n')
  print('Product of' ,num1 ,'and' ,num2 ,'is :',product, end = '\n')
  print('Division of ',num1 ,'and' ,num2 ,'is :',division, end = '\n')
  print('Modulus of ',num1 ,'and' ,num2 ,'is :',modulus)
  break
  except ValueError:
    print('You have to type an integer number! ')
