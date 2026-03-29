# Weekly-Challenge-10-Character-Battle
Double digits! For Week 10 of my coding challenge, I decided to build something fun: a mini RPG-style **Character Battle Simulator**.
Beneath the game-like exterior, this script is a practical exercise in managing **Dictionaries (Hash Maps)**, handling stochastic processes with `NumPy`, and applying control flow logic.

## How it works
1. **Stat Generation:** The algorithm iterates through a list of characters, assigning them random values for Strength, Intelligence, and Speed using `np.random.randint()`.
2. **Data Storage:** The generated stats, along with their calculated average, are stored in a nested Dictionary where the character's name is the Key.
3. **Random Matchmaking:** Using `np.random.choice(replace=False)`, the script fairly selects two unique fighters from the roster.
4. **The Battle:** The script retrieves the stored averages from the dictionary and compares them in $O(1)$ time to declare a winner.

## Complexity Analysis
* **Time Complexity:** $O(n)$ to generate and store the stats for $n$ characters. The matchmaking and battle comparison operate in $O(1)$ constant time.
* **Space Complexity:** $O(n)$ - We use a dictionary to store the attributes of all $n$ characters in memory.

## Code Snippet (Matchmaking & Battle)
```python
# Randomly select 2 unique characters
peleas = np.random.choice(personajes, size=2, replace=False)
contrincante1, contrincante2 = peleas[0], peleas[1]

# Extract stats from the Dictionary
promedio_c1 = estadisticas[contrincante1]["Promedio"]
promedio_c2 = estadisticas[contrincante2]["Promedio"]

# Declare the winner
if promedio_c1 > promedio_c2:
    print(f"The winner is {contrincante1}")
elif promedio_c2 > promedio_c1:
    print(f"The winner is {contrincante2}")


Dependencies
Python 3.14.3
NumPy
