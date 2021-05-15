/**
 * @author Hitesh Mishra
 * @email HiteshMishra708@gmail.com
 * @create date 2021-05-15 22:48:40
 * @modify date 2021-05-15 22:48:40
 * @desc [description]
 */
import camelcase

c = camelcase.CamelCase()
txt = "lorem ipsum dolor sit amet"
print(c.hump(txt))

#This method capitalizes the first letter of each word.