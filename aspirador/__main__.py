import sys

sys.path.append("/home/luisb/Documentos/GitHub/ia_2022")

from aspirador import agent, joc

def main():
    aspirador = agent.AspiradorMemoria()
    hab = joc.Casa([aspirador])
    hab.comencar()


if __name__ == "__main__":
    main()
