#Clases comienzan con mayuscula
#Variables con minusculas
class Operation:

    def _init_(self, _parametros=[]):
        self.parametros = _parametros

    def execute(self):
        print("Esta es una operacion")

class Suma(Operation):
    def execute(self):
        sum = self.parametros[0]+self.parametros[1]

        return sum

class Resta(Operation):
    def execute(self):
        rest = self.parametros[0]-self.parametros[1]
        return rest

class Division(Operation):
    def execute(self):
        if self.parametros[1]==0:
            print("No se puede realizar la operación")
        else:
            result = +self.parametros[0]/self.parametros[1]
            return result

class Multiplicacion(Operation):
    def _init_(self,  _parametros=[]):
        super()._init_(_parametros=_parametros)
    def execute(self):
        return self.parametros[0]*self.parametros[1]

class Fibonacci(Operation):
    def execute(self):
        n=self.parametros[0]
        if n<0:
            print("Invalido")
        elif n==0:
            return 0
        elif n==1:
            return 1
        else:
            fn_1 = Fibonacci([n-1])
            fn_2 = Fibonacci([n-2])
            return fn_1.execute(n-1)+fn_2.execute(n-2)

class Menu:
    def desplegar_menu(self):
        print("Introduzca la opcion deseada: ")
        print("1.-Sumar")
        print("2.-Restar")
        print("3.-Multiplicar")
        print("4.-Division")
        print("5.-Fibonacci")
        print("6.-Salir")

    def pedir_opcion(self):
        opcion_seleccionada = int(input())

    def validar_opcion(self,_opcion):
        opcion = int(input())
        if opcion <= 0:
            self.pedir_opcion()
        elif opcion <= 4:
            p1=int(input("Ingresa primer valor"))
            p2=int(input("Ingresa segundo valor"))
        elif opcion == 5:
            p1=int(input())
        elif opcion == 6:
            return None
        else:
            print("Opcion invalida")
            self.pedir_opcion()

    def ejecutar_operacion(self):
        pass



m1 = Menu()
m1.desplegar_menu()
opcion = m1.pedir_opcion()
m1.validar_opcion(opcion)
m1.pedir_parametros()
m1.ejecutar_operacion()
m1.mostrar_resultado()
print(resultado)

#Creacion de objetos para las subclases
#s = Suma()
#result = s.execute(5,6) #debe regresar 11
#print(result)

#r = Resta()
#res_rest = r.execute(7,2)#debe regresar 5
#print(res_rest)

#d = Division()
#result_d = d.execute(4,0)
#print(result_d)

#m = Multiplicacion()
#result_m = m.execute(5,2)
#print(result_m)