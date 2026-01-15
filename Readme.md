# Caffeine Visualizer

Visualizes **caffeine concentration in the body** over the day per user, based on drink intake data.

## Files

* `beverage_data.json` – caffeine content (mg/ml) for common drinks.
* `user_caffeine_intake_data.json` – user intake data: time, amount, and beverage.
* `visualize.py` – script that plots **individual intakes** and **cumulative caffeine** over the day.

## Requirements

* Python 3
* Packages: `numpy`, `matplotlib`

## How to Use

1. Open `visualize.py`.
2. Set `user_idx` to select a user and select if you want to show individual intake graphes (`show_individual=True`), cumulative graphs (`show_cumulative=True`) and the baseline (`show_baseline=True`).
3. Run the script:

```bash
python visualize.py
```

The script will show a plot of:

* Individual caffeine decay curves 
* Cumulative caffeine decayover the day 
* Baseline zero line

## How It Works

* Each intake is converted from **ml beverage → mg caffeine** using `beverage_data.json`.
* Caffeine decay is modeled as **1-Kompartiment with absorbation and decay** with a half-life of `4h`, a absorption rate of `1/h`, and a decay rate of `ln2/4`
* Curves are summed to show total caffeine in the body over time.

## Customization

* Change **half-life** in `visualize.py`: `CAFFEINE_HALF_LIFE_H`
* Change plot size: `WINDOW_WIDTH`, `WINDOW_HEIGHT`
* Toggle showing individual intakes: `show_individual=True
