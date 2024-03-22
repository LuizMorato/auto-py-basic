import pyautogui
import pandas
import time

from automate.password import password, email, link

def main():
    automate(link, email, password)
    read_db()

def automate(link, email, password):
    pyautogui.press("win")
    time.sleep(3)
    pyautogui.write("chrome")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)

    pyautogui.click(x=777, y=456)
    pyautogui.write(link)
    pyautogui.press("enter")
    time.sleep(3)

    pyautogui.click(x=866, y=324)
    time.sleep(2)
    pyautogui.write(email)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.write(password)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(3)

def read_db():
    table = pandas.read_csv("produtos.csv")

    for line in table.index:
        pyautogui.click(x=906, y=229)

        pyautogui.write(table.loc[line, 'codigo'])
        pyautogui.press('tab')

        pyautogui.write(table.loc[line, 'marca'])
        pyautogui.press('tab')

        pyautogui.write(table.loc[line, 'tipo'])
        pyautogui.press('tab')

        pyautogui.write(str(table.loc[line, 'categoria']))
        pyautogui.press('tab')

        pyautogui.write(str(table.loc[line, 'preco_unitario']))
        pyautogui.press('tab')

        pyautogui.write(str(table.loc[line, 'custo']))
        pyautogui.press('tab')

        obs = table.loc[line, 'obs']
        if not pandas.isna(obs):
            pyautogui.write(obs)
        
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.scroll(10000)


if __name__ == '__main__':
    main()