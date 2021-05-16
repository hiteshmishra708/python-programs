"""
 * @author Hitesh Mishra
 * @email HiteshMishra708@gmail.com
 * @create date 2021-05-16 15:42:39
 * @modify date 2021-05-16 15:42:39
 * @desc [description]
"""
#The try block will generate a NameError, because x is not defined:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")