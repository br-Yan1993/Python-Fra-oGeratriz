num_int = int(input("Digite a parte Inteira do numero (antes da virgula): "))
num_per = int(input("Digite o Período do numero (os numeros após a virgula): "))

def func_geratriz (n1, n2):
    geratriz1 = (n1 * 10 + n2 - n1)
    if (len(str(n2)) == 1):
        geratriz2 = 9
    elif (len(str(n2)) == 2):
        geratriz2 = 99
    elif (len(str(n2)) == 3):
        geratriz2 = 999
    elif (len(str(n2)) == 4):
        geratriz2 = 9999
    elif (len(str(n2)) == 5):
        geratriz2 = 99999
    elif (len(str(n2)) == 6):
        geratriz2 = 999999
    elif (len(str(n2)) == 7):
        geratriz2 = 9999999
    
    dizima = (geratriz1 / geratriz2)
    
    print("{}//{} = {}".format(geratriz1, geratriz2, dizima))

if __name__ == "__main__":
    func_geratriz(num_int, num_per)