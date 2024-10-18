import requests
import random
import time

# Fonction pour diviser les données en plusieurs parties
def split_data(data, n):
    k, m = divmod(len(data), n)
    return [data[i*k + min(i, m):(i+1)*k + min(i+1, m)] for i in range(n)]

# Fonction pour fusionner plusieurs listes triées
def merge(*lists):
    result = []
    for lst in lists:
        result = sorted(result + lst)  # Tri et fusion
    return result

# Envoyer une partie des données à trier à une machine distante
def send_to_machine(text_part, machine_url):
    response = requests.post(machine_url, json={'data': text_part})
    return response.json()

# Exemple de données
data = [random.randint(0, 1000000) for _ in range(10000)]

# Diviser les données en 3 parties
split_data = split_data(data, 3)

# Adresse des deux machines qui vont traiter les données
machine1_url = "http://192.168.1.33:5000/sort"
machine2_url = "http://192.168.1.35:5000/sort"

start = time.time()

# Mon PC 
sorted_part1 = sorted(split_data[0])

# Envoyer les deux parties à deux machines différentes pour qu'elles les trient
sorted_part2 = send_to_machine(split_data[1], machine1_url)
sorted_part3 = send_to_machine(split_data[2], machine2_url)

# Fusionner les résultats triés
final_sorted_data = merge(sorted_part1, sorted_part2, sorted_part3)

duration = time.time() - start

print("Temps d'exécution :", duration, "secondes")
print("Données triées :", final_sorted_data)

start2 = time.time()

l = sorted(data)

duration2 = time.time().start2 
print("Temps d'exécution d'une seule machine :", duration2, "secondes")