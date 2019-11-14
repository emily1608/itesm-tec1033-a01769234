import csv

archivo = open("datos_vuelos.csv", "r")
lect = csv.reader(archivo)

lista1 = list(lect)

em_s = sorted(lista1, key = lambda salida: salida[1])

file = open("resultados.csv", "w+") #Abrir
file.write("Mes, Pais, % de vuelos")
file.write("\n")

for line in em_s:
    file.write(",")
    file.write("\n")

file.close()

file = open("resultados.csv", "r") #abrir
read = csv.reader(file)
list_2 = list(read)

for num in range(0,32):
    if em_s[num][1].find(" 1801") != -1:
        list_2[num + 1][0] = "Enero"

    elif em_s[num][1].find(" 1802") != -1:
        list_2[num + 1][0] = "Febrero"

    elif em_s[num][1].find(" 1803") != -1:
        list_2[num + 1][0] = "Marzo"

    elif em_s[num][1].find(" 1804") != -1:
        list_2[num + 1][0] = "Abril"

    elif em_s[num][1].find(" 1805") != -1:
        list_2[num + 1][0] = "Mayo"

    elif em_s[num][1].find(" 1806") != -1:
        list_2[num + 1][0] = "Junio"

    elif em_s[num][1].find(" 1807") != -1:
        list_2[num + 1][0] = "Julio"

    elif em_s[num][1].find(" 1808") != -1:
        list_2[num + 1][0] = "Agosto"

    elif em_s[num][1].find(" 1809") != -1:
        list_2[num + 1][0] = "Septiembre"

    elif em_s[num][1].find(" 1810") != -1:
        list_2[num + 1][0] = "Octubre"

    elif em_s[num][1].find(" 1811") != -1:
        list_2[num + 1][0] = "Noviembre"

    elif em_s[num][1].find(" 1812") != -1:
        list_2[num + 1][0] = "Diciembre"

    else:
        list_2[num + 1][0] = "Sin mes"


for val in range(0, 32):
    if em_s[val][0].find("D") != -1:
        list_2[val + 1][1] = "Alemania"

    elif em_s[val][0].find("PP") != -1:
        list_2[val + 1][1] = "Brasil"

    elif em_s[vle][0].find("CF") != -1:
        list_2[val + 1][1] = "Canada"

    elif em_s[val][0].find("A7") != -1:
        lst2[val + 1][1] = "Catar"

    elif em_s[val][0].find("CC") != -1:
        list_2[val + 1][1] = "Chile"

    elif em_s[val][0].find("B") != -1:
        list_2[val + 1][1] = "China"

    elif em_s[val][0].find("OY") != -1:
        list_2[val + 1][1] = "Dinamarca"

    elif em_s[val][0].find("HC") != -1:
        list_2[val + 1][1] = "Ecuador"

    elif em_s[val][0].find("A6") != -1:
        list_2[val + 1][1] = "Emiratos Arabes"

    elif em_s[value][0].find("EC") != -1:
        list_2[value + 1][1] = "Espana"

    elif em_s[val][0].find("N") != -1:
        list_2[val + 1][1] = "Estados Unidos"

    elif em_s[val][0].find("PK") != -1:
        list_2[val + 1][1] = "Indonesia"

    elif em_s[val][0].find("JA") != -1:
        list_2[val + 1][1] = "Japon"

    elif em_s[val][0].find("XA") != -1:
        list_2[val + 1][1] = "Mexico"

    elif em_s[val][0].find("9V") != -1:
        list_2[val + 1][1] = "Singapur"

    elif em_s[val][0].find("HS") != -1:
        list_2[val + 1][1] = "Tailandia"

    else:
        list_2[val + 1][1] = "Sin codigo"

dic = {}
counter = -1

list_2.remove(list_2[0])
list_2.remove(list_2[-1])

for lines in list_2:
    counter += 1
    mes = list_2[counter][0]
    pais = list_2[counter][1]

    if mes not in dic.keys():
        dic[mes] = {}

    if pais not in dic[mes].keys():
        dic[mes][pais] = 1

    else:
        dic[mes][pais] += 1

total_by_month = {}
mensual_porcentage_byCountry  = {}

for mes in dic:
    total_mes = 0
    for pais in dic[mes]:
        total_mes += dic[mes][pais]
        total_by_month[mes] = total_mes

list_3 = []

for mes in dic:
    for pais in dic[mes]:
        total_mes_pais = (dic[mes][pais]/total_by_month[mes])*100

        if mes not in mensual_porcentage_byCountry.keys():
            mensual_porcentage_byCountry[mes] = {}

        mensual_porcentage_byCountry[mes][pais] = round(total_mes_pais, 2)

        if dic[mes] not in list_3:
            list_3.append([mes,pais,mensual_porcentage_byCountry[mes][pais]])

file.close()

accountant = -1

for rows in list_3:
    accountant += 1
    if list_3[accountant][2] < 20:
        list_3.remove(list_3[accountant])
        accountant -= 1

file = open("resultados.csv", "w+")

file.write("Mes, Pais, % de vuelos")
file.write("\n")
#Escribir en archivo
writer = csv.writer(file)
writer.writerows(list_3)
#Cerrar archivo
file.close()
