from appscript import app, mactypes
import requests
import random
import string

image_url = input("Enter the url of the img that you want to make wallpaper: ")

r = requests.get(image_url)
letters = string.ascii_lowercase
imgname= ''.join(random.choice(letters) for i in range(10))
with open(imgname+".png", 'wb') as f:
    f.write(r.content)

app('Finder').desktop_picture.set(mactypes.File('/Users/berilerken/Desktop/Python_Projects/'+imgname+".png/"))
