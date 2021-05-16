/**
 * @author Hitesh Mishra
 * @email HiteshMishra708@gmail.com
 * @create date 2021-05-16 15:40:23
 * @modify date 2021-05-16 15:40:23
 * @desc [description]
 */
import re

#Replace all white-space characters with the digit "9":

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)