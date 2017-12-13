import os

baseUrl = """ITEMNAME <br>
<video width="640” height="360" controls>
  <source src=“ITEMNAME.mp4” type="video/mp4">
</video>
<br><br>

"""

fullHtml = ""
ordedFiles = []

files = os.listdir(".")
#for file in files:
#    dotpos = file.index (".")
#    num = (file [:dotpos]).zfill(3)
#    restoffile = file [dotpos:]

files.sort()
for file in files:
	if file.endswith(".mp4"):
		fullHtml = fullHtml + baseUrl.replace("ITEMNAME", file [:-4])

print(fullHtml)