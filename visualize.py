import json

import matplotlib.pyplot as plt
import numpy as np

with open("user_caffeine_intake_data.json", "r") as f:
    user_caffeine_intake = json.load(f)
with open("beverage_data.json", "r") as f:
    beverages = json.load(f)  # Beverage:Coffein mg per ml


# caffeine_intake_mg = caffeine in mg at time 0
CAFFEINE_HALF_LIFE_H = 5
DECAY_CONSTANT = np.log(2) / CAFFEINE_HALF_LIFE_H  # because of T1/2=ln2/k=5
WINDOW_WIDTH = 12
WINDOW_HEIGHT = 6


def plot_caffeine_concentration_over_time_for_one_intake(
    caffeine_intake_ml, intake_time, user
):
    global DECAY_CONSTANT

    x = np.linspace(0, 24, 100)
    y = caffeine_intake_ml * np.exp(-DECAY_CONSTANT * (x - intake_time))

    x_plot = x[x >= intake_time]
    y_plot = y[x >= intake_time]

    plt.plot(x, np.zeros_like(x))
    plt.plot(x_plot, y_plot)
    plt.xlabel("Zeit t in Stunden nach 0 Uhr")
    plt.ylabel("Koffeingehalt in mg")
    plt.title(f"Koffeingehalt des Konsumenten {user} über den Tag")


def visualize_caffeine_concentration_for_all_caffein_intakes_of_a_user(user_idx):
    global WINDOW_HEIGHT, WINDOW_WIDTH

    user = user_caffeine_intake["users"][user_idx]["name"]
    plt.figure(figsize=(WINDOW_WIDTH, WINDOW_HEIGHT))

    for caffeine_intake_idx in range(0, 2):  # each caffeine intake
        intake_time = float(
            user_caffeine_intake["users"][user_idx]["caffeine_intake"][
                caffeine_intake_idx
            ]["time"]
        )
        amount_of_beverage_ml = user_caffeine_intake["users"][user_idx][
            "caffeine_intake"
        ][caffeine_intake_idx]["amount_ml"]
        beverage = user_caffeine_intake["users"][user_idx]["caffeine_intake"][
            caffeine_intake_idx
        ]["source"]
        beverage_caffeine_concentration_mg_per_ml = beverages[beverage]
        amount_of_caffeine_mg = (
            beverage_caffeine_concentration_mg_per_ml * amount_of_beverage_ml
        )

        plot_caffeine_concentration_over_time_for_one_intake(
            amount_of_caffeine_mg, intake_time, user
        )

    plt.show()


user_idx = 0
visualize_caffeine_concentration_for_all_caffein_intakes_of_a_user(user_idx)
