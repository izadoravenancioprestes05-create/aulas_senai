import sys
import time
import os
import platform


def shutdown():
    sistema = platform.system().lower()
    try:
        if "windows" in sistema:
            os.system("shutdows /s /t 0")
        elif "linux" in sistema or "darwin" in sistema:
            os.system("shutdown -h now")
        else:
            print("\n Sistema operacional não reconhecido")
    except Exception as e:
        print(f"\nError ao tentar o shutdown : {e}")

def temporizador_com_shutdown():
    print("=== Temporizador Trolator Tabajara === \n")
    try:
        entrada = int(input("\nQuantos segundos até o desligamento?"))
        segundos = int(entrada)

        while segundos > 0:
            mins, secs = divmod(segundos, 60)
            time = f"{mins:02d}:{secs:02d}"
            # Bip nos 10 segundos finais
        bip = "\a" if 0 < segundos < 10 else ""
        print(f"\r Tempo restante: {time}{bip}", end="", flush=True)
        time.sleep(1)
        segundos -= 1

        print("\n \nIniciando o desligamento... Tchau! ")

        shutdown()
    except ValueError:
        print("\nErro: Por favor, digite apenas números inteiros. ")
    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário.")


if __name__ == "__main__":
    temporizador_com_shutdown()