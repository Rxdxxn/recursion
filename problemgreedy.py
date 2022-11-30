# Având în vedere un set de sarcini cu termene limită și profitul total obținut la finalizarea unei sarcini, 
# găsiți profitul maxim obținut prin executarea sarcinilor în termenele specificate. 
# Să presupunem că o sarcină durează o unitate de timp pentru a fi executată și nu se poate executa după termenul limită.
# De asemenea, doar o singură sarcină va fi executată la un moment dat.

# O clasă pentru stocarea detaliilor postului. 
# Fiecare job are un identificator, un termen limită și un profit asociat.
class Lucru:
    def __init__(self, taskId, deadline, profit):
        self.taskId = taskId
        self.deadline = deadline
        self.profit = profit

if __name__ == '__main__':
 
    # Lista lucrurilor.Fiecare lucru are un identificator, 
    # un termen deadline limita si profit asociat acestuia.
    lucr = [
        Lucru(7, 5, 8), Lucru(2, 2, 2), Lucru(3, 5, 18), Lucru(9, 4, 12), Lucru(5, 4, 25),
        Lucru(6, 2, 20), Lucru(1, 9, 15), Lucru(8, 7, 10), Lucru(4, 7, 1), Lucru(10, 3, 5)
    ]
# stochează termenul maxim care poate fi asociat unei sarcini
    T=int(input('Dati termenul deadline pentru efectuarea sarcinii:'))
 
def planificare(lucruri, T):
    profit = 0
    slot = [-1] * T
 
    # aranjarea sarcnilor(lucrurilor) în ordinea descrescătoare a profiturilor lor
    lucr.sort(key=lambda x: x.profit, reverse=True)
 
    for lucru in lucr:
        for l in reversed(range(lucru.deadline)):
            if l < T and slot[l] == -1:
                slot[l] = lucru.taskId
                profit += lucru.profit
                break
 
    print('Lucrurile planificate', list(filter(lambda x: x != -1, slot)))
    print('Profitul total este', profit)
 

planificare(Lucru, T)

 


