# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import json


with open('spells.json', 'r') as spells_file:
    spells_data = json.load(spells_file)
    for spell in spells_data:
        img = Image.open('basecard.jpeg')
        I1 = ImageDraw.Draw(img)
        myFont = ImageFont.truetype('Arial Bold.ttf', 20)
        I1.text((10, 10), spell['title'], font=myFont, fill =(0, 0, 0))
        I1.text((10, 30), spell['level'], font=myFont, fill =(0, 0, 0))
        if spell['tradition']:
            I1.text((10, 60), spell['tradition'], font=myFont, fill =(0, 0, 0))
        else:
            pass
        details_len = len(spell['details'])
        x = 10
        for i in range(1, details_len):    
            print (x)
            I1.text((x, 90), spell['details'][i], font=myFont, fill =(0, 0, 0))
            x += len(spell['details'][i])

        img.save("images/{}.png".format(spell['title']))