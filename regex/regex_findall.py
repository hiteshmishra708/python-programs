/**
 * @author Hitesh Mishra
 * @email HiteshMishra708@gmail.com
 * @create date 2021-05-16 15:39:50
 * @modify date 2021-05-16 15:39:50
 * @desc [description]
 */
import re

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)