# Carrera de buses by @invalorable
# Discord: discord.gg/RFANGAzNM8

from time import sleep
import random, os

def carrera(b1, b2):
    print(40 * " " + "\x1b[0;31mCARRERA DE BUSES\n\n")
    output = ["-" * 100]
    output.extend(buses(b1, 1))
    output.extend(buses(b2, 2))
    return "\n".join(output)

def buses(pos, numero):
    return [
        (pos * " ") + " _______________  " + ((80 - pos) * " ") + "  |",
        (pos * " ") + "|__|__|__|__|__|___ " + ((80 - pos) * " ") + "|",
        (pos * " ") + f"|        {numero}        |)" + ((80 - pos) * " ") + "|",
        (pos * " ") + "|---@---------@---|)" + ((80 - pos) * " ") + "|",
        100 * "_"
    ]

a, b = 0, 0
ganador = None

while a < 82 and b < 82:
    if random.randint(1, 2) == 1:
        a += 1
    else:
        b += 1
    
    os.system("cls" if os.name == "nt" else "clear")
    os.system('title Carrera de buses [Made by @invalorable]')
    print(carrera(a, b))
    sleep(0.07)

ganador = "1" if a >= 81 else "2" if b >= 81 else None
print(f"\n EL BUS {ganador} GANÓ LA CARRERA")
sleep(5)
exit()