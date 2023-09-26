import pyautogui
from time import sleep
pyautogui.click(763,1056,duration=2)
pyautogui.click(805,253,duration=2)
pyautogui.write('SAMUEL')
pyautogui.click(827,312,duration=0.1)
pyautogui.write('0058543')
pyautogui.click(823,380,duration=0.1)
pyautogui.write('NEWPALACE')
pyautogui.click(831,463,duration=0.1)
pyautogui.write('XE2')
pyautogui.click(954,526,duration=2)
pyautogui.click(336,43,duration=3)
pyautogui.click(1912,114,duration=2)
pyautogui.click(1767,75,duration=3)
pyautogui.click(360,95,duration=2)
pyautogui.click(377,299,duration=0.5)
pyautogui.click(510,587,duration=2)
#adicionando itens
with open('test.txt','r') as arquivo:
    for linha in arquivo:
      produto = linha.split(',')[0]
      
      pyautogui.write(produto)
      pyautogui.click(559,528,duration=0.5)
      pyautogui.click(478,673,duration=0.5)
      pyautogui.click(479,531,duration=0.5)    
      pyautogui.moveTo(466,589, duration=0.2)
      pyautogui.dragRel(400,0, duration=0.2)
      pyautogui.press('delete')
sleep(1)
pyautogui.click(1432,487, duration=1)
pyautogui.click(842,393, duration=1)
with open('test.txt','r') as arquivo:
    for linha in arquivo:
      quantidade = linha.split(',')[1]
      pyautogui.write(quantidade)
      sleep(0.1)