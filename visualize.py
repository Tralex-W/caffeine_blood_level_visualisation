import json

import matplotlib.pyplot as plt
import numpy as np

with open("user_caffeine_intake_data.json", "r") as f:
    user_caffeine_intake = json.load(f)
with open("beverage_data.json", "r") as f:
    beverages = json.load(f)  # Beverage:Coffein mg per ml


# caffeine_intake_mg = caffeine in mg at time 0
decay_constant = 0.1385  # decay_constant = 0.1385 = ln2/5, because of T1/2=ln2/k=5


def visualize_caffeine_concentration_over_time(caffeine_intake_ml, intake_time, user):
    global decay_constant

    x = np.linspace(0, 24, 100)
    y = caffeine_intake_ml * np.exp(-decay_constant * (x - intake_time))

    x_plot = x[x >= intake_time]
    y_plot = y[x >= intake_time]

    plt.plot(x, np.zeros_like(x))
    plt.plot(x_plot, y_plot)
    plt.xlabel("Zeit t in Stunden nach 0 Uhr")
    plt.ylabel("Koffeingehalt in mg")
    plt.title(f"Koffeingehalt des Konsumenten {user} über den Tag")
    plt.show()


user_idx = 0
caffeine_intake_idx = 0


user = user_caffeine_intake["users"][user_idx]["name"]
intake_time = float(
    user_caffeine_intake["users"][user_idx]["caffeine_intake"][caffeine_intake_idx][
        "time"
    ]
)
amount_of_beverage_ml = user_caffeine_intake["users"][user_idx]["caffeine_intake"][
    caffeine_intake_idx
]["amount_ml"]
beverage = user_caffeine_intake["users"][user_idx]["caffeine_intake"][
    caffeine_intake_idx
]["source"]
beverage_caffeine_concentration_mg_per_ml = beverages[beverage]
amount_of_caffeine_mg = (
    beverage_caffeine_concentration_mg_per_ml * amount_of_beverage_ml
)


visualize_caffeine_concentration_over_time(amount_of_caffeine_mg, intake_time, user)
