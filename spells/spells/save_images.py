# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from cairosvg import svg2png
import json
import itertools
import textwrap

#image size 500x689
with open('spells.json', 'r') as spells_file:
    spells_data = json.load(spells_file)
    tradition_name = ""
    for spell in spells_data:
        tradition_len = len(spell['tradition'])
        if spell['tradition']:
            for i in range(0, tradition_len):
                match spell['tradition'][i]:
                    case "Ocultista":
                        img = Image.open('occultist_basecard.jpeg')
                    case "Arcana":
                        img = Image.open('arcane_basecard.jpeg')
                    case "Divina":
                        img = Image.open('divine_basecard.jpeg')
                    case "Primal":
                        img = Image.open('primal_basecard.jpeg')
                tradition_name=spell['tradition'][i]
        else:
            img = Image.open('focus_basecard.jpg')
        I1 = ImageDraw.Draw(img)
        line_color = (0, 0, 0)
        myFont = ImageFont.truetype('Arial Bold.ttf', 20)
        title_font = ImageFont.truetype('Mark Simonson  Proxima Nova Extra Condensed Bold TheFontsMaster.com.otf', 40)
        stats_font = ImageFont.truetype('Mark Simonson  Proxima Nova Extra Condensed Bold TheFontsMaster.com.otf', 30)
        tags_font = ImageFont.truetype('Mark Simonson  Proxima Nova Extra Condensed Bold TheFontsMaster.com.otf', 15)

        # Title
        I1.text((30, 20), spell['title'].upper(), font=title_font, fill =(0, 0, 0))

        #Level
        I1.text((700, 20), spell['level'].upper(), anchor="ra", font=title_font, fill =(0, 0, 0))
        draw = ImageDraw.Draw(img) 
        draw.line((30,70, 700,70), fill=line_color, width=2)

        #Tags
        tags_len = len(spell['tags'])
        x = 30
        for i in range(0, tags_len):
            position = (x, 80)
            left, top, right, bottom = I1.textbbox(position, spell['tags'][i].upper(), font=tags_font)
            I1.rectangle((left-5, 85-5, right+5, 95+5), fill=(114,18,20))
            I1.text(position, spell['tags'][i].upper(), font=tags_font, fill="white")
            x += (I1.textlength(spell['tags'][i].upper(), font=tags_font)+20)
        
        # #Action
        if spell['action']:
            match spell['action'][0]:
                case """<svg xmlns="http://www.w3.org/2000/svg" style="height:1em;width:1.53em;font-size:0.9em" viewbox="0 0 153 100"><defs></defs><path fill="black" d="M23 34l16 16-16 16L8 50zm0 0l16 16-16 16L8 50zm0 0l16 16-16 16L8  50zM51 6L30 27l22 23-22 23 21 21 44-44zm0 0L30 27l22 23-22 23 21  21 44-44zm0 0L30 27l22 23-22 23 21 21 44-44zm56 5L88 30l20 19-20 20 19 19 38-39z"></path></svg>""":
                    action = Image.open("two_actions.png").convert("RGBA")
                case """<svg xmlns="http://www.w3.org/2000/svg" style="height:1em;width:1em;font-size:0.9em" viewbox="0 0 100 100"><defs></defs><path fill="black" d="M22 34l16 16-16 16L7 50zM50 6L29 27l22 23-22 23 21 21 43-44z"></path></svg>""":
                    action = Image.open("one_action.png").convert("RGBA")
                case """<svg xmlns="http://www.w3.org/2000/svg" style="height:1em;width:1em;font-size:0.9em" viewbox="0 0 100 100"><defs></defs><path fill="black" d="M52 72l4-1a32 32 0 008-5 28 28 0 006-8 17 17 0 002-4 19 19 0 001-6 20 20 0 00-3-9 26 26 0 00-10-9 45 45 0 00-11-5 52 52 0 00-9-1 50 50 0 00-10 0 53 53 0 00-11 4 36 36 0 00-8 4 29 29 0 00-3 2l-2 3a30 30 0 016-10 34 34 0 016-5 45 45 0 0110-6 58 58 0 0111-2 68 68 0 0111-1 56 56 0 0110 1 45 45 0 019 2 50 50 0 017 3 47 47 0 017 5 33 33 0 016 6 28 28 0 013 6 23 23 0 012 9 21 21 0 01-1 6 31 31 0 01-3 7 31 31 0 01-6 6 44 44 0 01-6 5 48 48 0 01-7 3 44 44 0 01-12 4h-6l8 11-41-9 36-23z"></path></svg>""":
                    action = Image.open("reaction.png").convert("RGBA")
                case """<svg xmlns="http://www.w3.org/2000/svg" style="height:1em;width:1em;font-size:0.9em" viewbox="0 0 100 100"><defs></defs><path fill="black" d="M93 50L50 94 7 51 50 6zm-71-1l10 9 9-9-9-10zm18-20l21 21-22 21 10 10 32-32-31-31z"></path></svg>""":
                    action = Image.open("free_action.png").convert("RGBA")
                case """<svg xmlns="http://www.w3.org/2000/svg" style="height:1em;width:2.03em;font-size:0.9em" viewbox="0 0 203 100"><defs></defs><path fill="black" d="M27 34l15 16-15 16-16-16zm0 0l15 16-15 16-16-16zm0 0l15 16-15 16-16-16zM54 6L33 27l23 23-23 23 21 21 44-44zm0 0L33 27l23 23-23 23 21 21 44-44zm0 0L33 27l23 23-23 23 21 21 44-44zm56 5L91 30l20 19-20 20 19 19 39-39zm51 8l-14 14 15 16-15 16 14 15 31-31z"></path></svg>""":
                    action = Image.open("three_actions.png").convert("RGBA")
            width, height = action.size
            newsize = (round(width/3), round(height/3))
            action = action.resize(newsize)
            I1.text((30, 120), "Execução ", font=stats_font, fill =(0, 0, 0))
            x = (I1.textlength("Execução ", font=stats_font)+30)
            img.paste(action, (round(x), 120), action)
        
        #Details
        details_len = len(spell['details'])
        x = 30
        y = 170
        list_of_components = ['material', 'somático', 'verbal']
        distance = ['metros', 'metro', 'toque', 'quilômetros', 'quilômetro']
        area = ['explosão']
        duração = ['sustentada', 'minuto', 'minutos', 'mês', 'dias', 'dias', 'meses', 'hora', 'horas']
        alvo = ['criatura', 'criaturas', 'objeto', 'objetos']
        if spell['details']:
            for i in range(1, details_len):
                new_string = spell['details'][i].replace(' ', ',').replace('.', ',').replace(';', ',')
                list_of_spell_components = new_string.split(',')
                result = [i for i in list_of_components if i in list_of_spell_components]
                if result:
                    I1.text((180, 120), spell['details'][i], font=stats_font, fill =(0, 0, 0))
                else:
                    result = [i for i in distance if i in list_of_spell_components]
                    dif_area = [i for i in list_of_spell_components if i in area]
                    dif_alvo = [i for i in list_of_spell_components if i in alvo]
                    print(list_of_spell_components)
                    print(dif_alvo)
                    if result and not dif_area and not dif_alvo:
                        I1.text((30, 150), "Distância {}".format(spell['details'][i]), font=stats_font, fill =(0, 0, 0))
                    elif result and dif_area:
                        I1.text((30, 180), "Área {}".format(spell['details'][i]), font=stats_font, fill =(0, 0, 0))
                result = [i for i in duração if i in list_of_spell_components]
                if result:
                    I1.text((30, 210),"Duração {}".format(spell['details'][i]), font=stats_font, fill =(0, 0, 0))
        # for i in range(1, details_len):
        #     match i:
        #         case 1:
        #             I1.text((180, 120), spell['details'][i], font=stats_font, fill =(0, 0, 0))
        #         case 2:
        #             I1.text((x, y), spell['details'][i], font=stats_font, fill =(0, 0, 0))
            #x += (len(spell['details'][i]))
            y += 30

        # #Description
        # if spell['description']:
        #     lines = textwrap.wrap(spell['description'], width=40)
        #     y_text = 120
        #     for line in lines:
        #         width, height = myFont.getsize(line)
        #         I1.text(((500 - width) / 2, y_text), line, font=myFont, fill =(0, 0, 0))
        #         y_text += height

  

        img.save("images/{}_{}.png".format(spell['title'],tradition_name))