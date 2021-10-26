import pyqrcode

s = "https://www.youtube.com/c/TurtleCode/videos"

url = pyqrcode.create(s)

url.svg("myyoutube.svg", scale=8)