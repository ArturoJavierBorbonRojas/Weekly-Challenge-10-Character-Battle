import numpy as np

# Weekly Challenge 10: Character Battle
# Author: Ing. Arturo Javier Borbon Rojas

# 1 List of characters
personajes= ["Jim", "Tom", "Jerry", "Luke", "Jeff", "Kerry"]

# 1.1 Create empty dictionary to save character statistics
estadisticas= {}


# 2 Create attributes for each character
for personaje in personajes:
    fuerza= np.random.randint(0,10)
    inteligencia= np.random.randint(0,10)
    velocidad= np.random.randint(0,10)
    promedio= (velocidad+ inteligencia+ fuerza)/ 3

    # 2.1 Save statistics
    estadisticas[personaje]={
        "Fuerza":fuerza,
        "Inteligencia": inteligencia,
        "velocidad": velocidad,
        "Promedio": promedio
    }
     # 2.2 Print statistics 
    print(f"""The character {personaje} has the following stats:
            strength:{fuerza}, 
            intelligence:{inteligencia}, 
            speed:{velocidad} """)
    print("Average: ", promedio)
    print("------------------")


# 3 Select two characters for a fight 
# 3.1 Use random choice without replace to pick 2 characters
peleas= np.random.choice(personajes,size=2, replace=False)
# 3.2 Save the two characters
contrincante1= peleas[0]
contrincante2= peleas[1]
print(f"The fighters for the match are {peleas[0]} vs {peleas[1]}")
print("-------------------------")

# 3.3 Extract the average from the dictionary for each fighter
promedio_c1 = estadisticas[contrincante1]["Promedio"]
promedio_c2 = estadisticas[contrincante2]["Promedio"]

print(f"The character {contrincante1} has an average of {promedio_c1}")
print(f"The character {contrincante2} has an average of {promedio_c2}")


# 4 Compare averages to pick a winner
if promedio_c1 <promedio_c2:
    print(f"The winner is {contrincante2}")
elif promedio_c2<promedio_c1:
    print(f"The winner is {contrincante1}")
else:
    print("It's a tie")

print("--------------------------------")