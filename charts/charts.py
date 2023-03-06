import matplotlib.pyplot as plt

def generate_pie_char():
    labels = ['A','B','C']
    values = [200,34,120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('.pi.png')
    plt.close()