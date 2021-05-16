/**
 * @author Hitesh Mishra
 * @email HiteshMishra708@gmail.com
 * @create date 2021-05-16 15:39:35
 * @modify date 2021-05-16 15:39:35
 * @desc [description]
 */
import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")