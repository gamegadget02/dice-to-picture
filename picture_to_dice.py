from PIL import Image

image = Image.open("dice picture\photo-1506794778202-cad84cf45f1d.jpg")
imagebw = image.convert("L")
imagebw.save("temp.jpg", quality=1)
imagebwlow = Image.open("temp.jpg", "r")
imagebwlow.show()
width,hight = imagebwlow.size
print(hight)
print(width)
pix_val = list(imagebwlow.getdata())
f = open("dice picture\output.txt", "w")
r=0
for a in pix_val:
    r+=1
    if r == width:
        f.write("\n")
        f.write(str(a))
        r=1
    else:
        f.write(str(a))
f.close()
print(pix_val)