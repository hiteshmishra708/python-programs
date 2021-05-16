/**
 * @author Hitesh Mishra
 * @email HiteshMishra708@gmail.com
 * @create date 2021-05-16 15:39:57
 * @modify date 2021-05-16 15:39:57
 * @desc [description]
 */
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())