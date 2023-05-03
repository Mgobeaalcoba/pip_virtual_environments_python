import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ["A", "B", "C"]
    values = [200,34,120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    # Comando para guardar nuestro chart directamente
    plt.savefig("pie.png")
    # Cierro plt luego de guardar. 
    plt.close()
    # plt.show() se usa para mostrar el grafico sin guardarlo. 