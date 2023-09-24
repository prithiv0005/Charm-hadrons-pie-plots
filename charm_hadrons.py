import matplotlib.pyplot as plt

# Define data for charm hadrons (replace with actual data)
charm_hadrons = [
    {"name": "D+ Meson (D⁺)", "composition": {"c": 1, "u": 1}, "lifetime": 1.04},
    {"name": "D- Meson (D⁻)", "composition": {"c": 1, "d": 1}, "lifetime": 1.06},
    {"name": "D0 Meson (D⁰)", "composition": {"c": 1, "u": 1}, "lifetime": 0.41},
    {"name": "D0-bar Meson (D⁰̅ )", "composition": {"c̅": 1, "u̅": 1}, "lifetime": 0.41},
    {"name": "Lambda_c+ Baryon (Λc⁺)", "composition": {"c": 1, "u": 1, "d": 1}, "lifetime": 20.02},
    {"name": "Lambda_c-bar Baryon (Λc̅)", "composition": {"c̅": 1, "u̅": 1, "d̅": 1}, "lifetime": 20.2},
    {"name": "Xi_c+ Baryon (Ξc⁺)", "composition": {"c": 1, "u": 1, "s": 1}, "lifetime": 51.6},
    {"name": "Xi_c0 Baryon (Ξc⁰)", "composition": {"c": 1, "u": 1, "s": 1}, "lifetime": 59.9},
    {"name": "Omega_c0 Baryon (Ωc⁰)", "composition": {"c": 1, "s": 2}, "lifetime": 75.8},
    {"name": "Omega_c+ Baryon (Ωc⁺)", "composition": {"c": 1, "s": 2}, "lifetime": 2.9},
]

# Create a directory for saving plots (optional)
import os
if not os.path.exists("charm_hadron_plots"):
    os.makedirs("charm_hadron_plots")

# Create pie charts for each charm hadron
for hadron in charm_hadrons:
    composition = hadron["composition"]
    lifetime = hadron["lifetime"]

    # Prepare data for the pie chart
    labels = composition.keys()
    sizes = composition.values()

    # Create the pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f"{hadron['name']} (Lifetime: {lifetime} ps)")

    # Save the pie chart as an image (optional)
    plt.savefig(f"charm_hadron_plots/{hadron['name']}_pie_chart.png")

    # Display the pie chart
    plt.show()

# Note: Replace the data in charm_hadrons with actual values from the PDG.

# You can run this script, and it will generate pie charts for each charm hadron
# with quark compositions and lifetimes. The charts will be saved in the "charm_hadron_plots" directory.

