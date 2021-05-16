"""
 * @author Hitesh Mishra
 * @email HiteshMishra708@gmail.com
 * @create date 2021-05-16 15:47:29
 * @modify date 2021-05-16 15:47:29
 * @desc [description]
"""
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))