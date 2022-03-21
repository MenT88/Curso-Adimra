"""
ejercicio ronda personas
"""

PERSONAS = 10
LIMITE_CUENTA = 25

cuenta = 0
persona = 0
giro = "horario"


for ciclo in range(LIMITE_CUENTA):
    cuenta = cuenta + 1 #contador general
    
    if (giro == "horario"):
        if (persona == PERSONAS):
            persona = 0
        persona = persona + 1 #contador de personas
    else:
        if (persona == 1):
            persona = PERSONAS + 1
        persona = persona - 1
    
    print(cuenta, persona)    

    if (cuenta % 8 == 0): #es pefect divisible por 8
        if (giro == "horario"):
            giro = "antihorario"
        else:
            giro = "horario"    

   
    
  
    

