import json

import matplotlib.pyplot as plt
import numpy as np

with open("user_coffein_intake_data.json", "r") as f:
    data = json.load(f)

print(data)
print(data["users"][0])


# start_value = Coffein in ml at time 0
# decay_constant = ln2/5, because of T1/2=ln2/k=5
def visualize_coffein(start_value, decay_constant, user):
    start_value = 150
    decay_constant = 0.1385

    x = np.linspace(0, 24, 100)
    y = start_value * np.exp(-decay_constant * x)

    plt.plot(x, y)
    plt.xlabel("Zeit t in Stunden nach der ersten Koffeineinnahme")
    plt.ylabel("Koffeingehalt in mg")
    plt.title(f"Koffeingehalt des Konsumenten ${user} über den Tag")
    plt.show()
