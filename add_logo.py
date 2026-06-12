from PIL import Image

def make_transparent(img):
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        # If the pixel is dark (black-ish), make it transparent
        if item[0] < 50 and item[1] < 50 and item[2] < 50:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    return img

base = Image.open('foto/masa_sekarang.png').convert('RGBA')
logo = Image.open('C:/Users/HP/.gemini/antigravity-ide/brain/3a252e0f-2bd0-42fb-b32e-a1edcc4a8955/media__1781198498995.jpg')

logo = make_transparent(logo)
logo = logo.resize((100, 100))

# Try placing it around where a left chest would be for a character on the left
x, y = 350, 550
base.paste(logo, (x, y), logo)

base.convert('RGB').save('foto/masa_sekarang.png')
print('Done!')
