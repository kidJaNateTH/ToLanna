"""
สำฮับใครตี่เป็นจาวเหนือ
สามารถเพิ่มคำเหนือตี่หมู่ตั๋วกิ้ดได้เด้อ
แล้วเอามาแบ่งปันกันผ่องน้อ ToLanna ของหมู่เฮาจะได้มีความแม่นยำมากขึ้น - kidjanate
"""


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

me = {
    "ฉัน" : "เปิ้ล",
    "ฉัน" : "เปิ้น",
    "เรา" : "เฮา",
    "กู" : "ฮา",
    "ชั้น" : "เปิ้ล",
    "ชั้น" : "เปิ้น",
    "พี่" : "อ้าย",
    "เธอ" : "ตั่ว"
}

you = {
    "นาย" : "คิง",
    "เธอ" : "ตั๋ว",
    "อี" : "อี่",
    "คุณ" : "ตั๋ว"
}

others = {
    "พูด" : "อู้",
    "รู้" : "ฮู้",
    "เรียน" : "เฮียน",
    "บ้าง" : "ผ่อง",
    "มั้ย" : "ก่",
    "ไหม" : "ก่อ",
    "ล่ะ" : "เลาะ",
    "รัก" : "ฮัก",
    "โง่" : "ง่าว",
    "ไม่" : "บ่",
    "ทำ" : "ยะ",
    "แบบ" : "จะ",
    "นี่" : "อี้",
    "นะ" : "เด้อ",
    "ให้" : "หื้อ",
    "ดู" : "ผ่อ",
    "สิ" : "เลาะ",
    "เที่ยว" : "แอ่ว",
    "หรอ" : "อี้",
    "อร่อย" : "ลำ",
    "อะไรอีก" : "อะหยังแหมเมาะ",
    "อะไร" : "อะหยัง",
    "รถมอเตอร์ไซค์" : "รถเครื่อง",
    "ใช่" : "ใจ๋",
    "ใช่" : "ใจ้",
    "ใช่" : "ไจ่",
    "ใช่" : "ไจ้",
    "ค่ะ" : "จ้าว",
    "คะ" : "เจ้า",
    "สนุก" : "ม่วน",
    "มาก" : "ขนาด",
    "สวย" : "งาม",
    "นาน" : "เมิน",
    "ใช้" : "ใจ้",
    "บ่น" : "จ่ม",
    "ขอโทษ" : "สุมาเต๊อะ",
    "ผู้ชาย" : "ป้อจาย",
    "ผู้หญิง" : "แม่ญิง",
    "เหนื่อย" : "อิด",
    "อยาก" : "ใคร่",
    "อยาก" : "ใคร่อยาก",
    "อ้วก" : "ฮาก",
    "อย่างไร" : "จะใด",
    "เคย" : "เกย",
    "ด้วย" : "โตย",
    "กัน" : "กั๋น",
    "เป็น" : "เป่น",
    "ทาง" : "ตาง",
    "ที่" : "ตี่",
    "ทุก" : "ตึง",
    "จริง" : "แต้",
    "จริง" : "แต๊",
    "ขนาด" : "ม๊อก",
    "แรง" : "แฮง"
    
}

family = {
    "พ่อ" : "ป้อ",
}

times = {
    "เมื่อวาน" : "ตะวา",
    "พรุ่งนี้" : "วันพูก",
    "อาทิตย์หน้า" : "ติ้ดหน้า",
    "ตอนเย็น" : "ตอนแลง",
    "ตอนเช้า" : "ตอนเจ้า",
}

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
        newText = newText.replace("ไม่ะ","ไม่")

    return newText