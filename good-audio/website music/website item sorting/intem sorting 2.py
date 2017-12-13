import os

baseUrl = """ITEMNAME <br>
<audio controls>
<source src="earape/ITEMNAME.mp3" type="audio/mpeg">
</audio><br>
<br>
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
	if file.endswith(".mp3"):
		fullHtml = fullHtml + baseUrl.replace("ITEMNAME", file [:-4])

print(fullHtml)