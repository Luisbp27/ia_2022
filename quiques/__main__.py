import sys

sys.path.append("/home/luisb/Documentos/GitHub/ia_2022")

from quiques import agent_amplada, agent_profunditat, joc


def main():
    barca = agent_amplada.BarcaAmplada()
    illes = joc.Illes([barca])
    illes.comencar()


if __name__ == "__main__":
    main()
