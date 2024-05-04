import pyautogui as pa
from time import sleep



pa.press('win')
sleep(1.5)
pa.write('anki')
sleep(1)
pa.press('enter')
pa.sleep(7)
pa.click(x=1207, y=459)
pa.sleep(3)

with open('texto.txt','r',encoding='utf-8') as file:
    textArray = file.readlines()

for i in range(0,len(textArray),2):
    word = textArray[i]
    key = textArray[i+1]
    sleep(0.8)

    pa.write(f'{word}')#primeira linha
    pa.sleep(0.6)
    pa.press('tab')
    pa.sleep(1)
    pa.write(f'{key}')#segunda linha
    sleep(0.6)
    pa.click(x=1896, y=1159)
    sleep(1)





pa.click(x=2076, y=1158)

