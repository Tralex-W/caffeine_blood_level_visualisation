import json

import matplotlib.pyplot as plt
import numpy as np

with open("user_caffeine_intake_data.json", "r") as f:
    user_caffeine_intake = json.load(f)
with open("beverage_data.json", "r") as f:
    beverages = json.load(f)  # Beverage:Coffein mg per ml


# caffeine_intake_mg = caffeine in mg at time 0
CAFFEINE_HALF_LIFE_H = 4
DECAY_CONSTANT = np.log(2) / CAFFEINE_HALF_LIFE_H  # because of T1/2=ln2/k=5
WINDOW_WIDTH = 12
WINDOW_HEIGHT = 6
X_LINSPACE = np.linspace(0, 24, 100)
ABSORBATION_RATE = 1
cumulative_caffeine_plot = np.zeros_like(X_LINSPACE)


def plot_caffeine_concentration_over_time_for_one_intake(
    caffeine_intake_mg, intake_time, label, show_individual=True
):
    global DECAY_CONSTANT, X_LINSPACE, ABSORBATION_RATE, cumulative_caffeine_plot

    y = (
        (caffeine_intake_mg * ABSORBATION_RATE)
        / (ABSORBATION_RATE - DECAY_CONSTANT)
        * (
            np.exp(-DECAY_CONSTANT * (X_LINSPACE - intake_time))
            - np.exp(-ABSORBATION_RATE * (X_LINSPACE - intake_time))
        )
    )

    cumulative_caffeine_plot += np.where(X_LINSPACE >= intake_time, y, 0)

    x_plot = X_LINSPACE[X_LINSPACE >= intake_time]
    y_plot = y[X_LINSPACE >= intake_time]

    if show_individual:
        plt.plot(x_plot, y_plot, label=label)
    plt.xlabel("Zeit t in Stunden nach 0 Uhr")
    plt.ylabel("Koffeingehalt in mg")


def visualize_caffeine_concentration_for_all_caffein_intakes_of_a_user(
    user_idx, show_null=True, show_accumulated=True, show_individual=True
):
    global WINDOW_HEIGHT, WINDOW_WIDTH

    user = user_caffeine_intake["users"][user_idx]["name"]
    plt.figure(figsize=(WINDOW_WIDTH, WINDOW_HEIGHT))

    number_of_caffein_intakes = len(
        user_caffeine_intake["users"][user_idx]["caffeine_intake"]
    )

    for caffeine_intake_idx in range(
        0, number_of_caffein_intakes
    ):  # each caffeine intake
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
            amount_of_caffeine_mg,
            intake_time,
            f"Einnahme {caffeine_intake_idx + 1}",
            show_individual=show_individual,
        )

    if show_accumulated:
        plt.plot(X_LINSPACE, cumulative_caffeine_plot, label="Kumulativ")
    if show_null:
        plt.plot(X_LINSPACE, np.zeros_like(X_LINSPACE), label="Null")
    plt.title(f"Koffeingehalt des Konsumenten {user} über den Tag")
    plt.legend()
    plt.show()


user_idx = 0
visualize_caffeine_concentration_for_all_caffein_intakes_of_a_user(
    user_idx, show_null=True, show_accumulated=True, show_individual=False
)
