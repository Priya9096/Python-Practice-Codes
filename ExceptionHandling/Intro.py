def disp(a,b):
   try:
      print('Task Started')
      print(a/b)
   except:
      print('Some error Handled')
   else:
      print('Task Executed without any execption')
   finally:
      print('Task Ended')
   
disp(10,0)
disp(10,5)
disp(20,2)