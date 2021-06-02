"""
สำฮับใครตี่เป็นจาวเหนือ
สามารถเพิ่มคำเหนือตี่หมู่ตั๋วกิ้ดได้เด้อ
แล้วเอามาแบ่งปันกันผ่องน้อ ToLanna ของหมู่เฮาจะได้มีความแม่นยำมากขึ้น - kidjanate
"""
# -*- coding: utf-8 -*-
import json
jsontext = open("words.json","r",encoding="utf-8").read()
j = json.loads(jsontext)

me = j["me"]
you = j["you"]
family = j["family"]
numbers = j["numbers"]
others = j["others"]
times = j["times"]

def ToLanna(CoolContent):
    """
    Convert Thai to Lanna
    """
    return _backend(CoolContent, True)

def ToThai(CoolContent):
    """
    Convert Lanna to Thai
    """
    return _backend(CoolContent, False)


def _backend(CoolContent:str, isMuang):
    newText = CoolContent

    if isMuang:
        for i in you.keys():
            newText = newText.replace(i,you[i])

        for i in me.keys():
            newText = newText.replace(i,me[i])

        for i in others.keys():
            newText = newText.replace(i,others[i])

        for i in times.keys():
            newText = newText.replace(i,times[i])
        
        for i in family.keys():
            newText = newText.replace(i,family[i])

        for i in numbers.keys():
            newText = newText.replace(i,numbers[i])
    else:
        for key, val in you.items():
            if newText.find(val) != -1:
                newText = newText.replace(val,key)

        for key, val in me.items():
            if newText.find(val) != -1:
                newText = newText.replace(val,key)

        for key, val in others.items():
            if newText.find(val) != -1:
                newText = newText.replace(val,key)

        for key, val in times.items():
            if newText.find(val) != -1:
                newText = newText.replace(val,key)

        for key, val in family.items():
            if newText.find(val) != -1:
                newText = newText.replace(val,key)

        for key, val in numbers.items():
            if newText.find(val) != -1:
                newText = newText.replace(val,key)
        newText = newText.replace("ไม่ะ","ไม่")

    return newText
