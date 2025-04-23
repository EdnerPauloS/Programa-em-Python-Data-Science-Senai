import statistics
import matplotlib.pyplot as plt 


medias_jose = [10,5,8,9,10,5,4]


meses = ['fev','mar', 'abril', 'maio', 'junho', 'julho', 'agosto']


def grafico_plot():
    plt.figure(figsize=(6,4))
    plt.bar(meses, medias_jose)
    plt.plot(meses, medias_jose, color='red', marker='o')
    plt.title('média notas ')
    plt.grid()
    plt.xlabel('meses')
    plt.ylabel('medias')
    plt.show()


grafico_plot()



# def grafico_bar():




# grafico_bar()



# def grafico_pie():


  


# grafico_pie()



# def grafico_scatter():


    


# grafico_scatter()


