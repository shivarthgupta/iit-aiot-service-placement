import os
import matplotlib.pyplot as plt


# Results from our experiments
methods = [
    "Baseline",
    "PPO-1",
    "PPO-2",
    "PPO-3",
    "PPO-4"
]

success_rate = [
    81.50,
    54.50,
    35.00,
    45.50,
    28.50
]

average_latency = [
    40.74,
    38.35,
    36.24,
    37.86,
    35.61
]

reliability = [
    0.9029,
    0.8978,
    0.9010,
    0.8912,
    0.8883
]


# Create output folder
output_folder = "results/graphs"

os.makedirs(
    output_folder,
    exist_ok=True
)


# -----------------------------------------
# Graph 1: Placement Success Rate
# -----------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    methods,
    success_rate
)

plt.xlabel("Method")
plt.ylabel("Placement Success Rate (%)")

plt.title(
    "Service Placement Success Rate"
)

plt.ylim(0, 100)

plt.tight_layout()

plt.savefig(
    f"{output_folder}/placement_success_rate.png",
    dpi=300
)

plt.close()


# -----------------------------------------
# Graph 2: Average Latency
# -----------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    methods,
    average_latency
)

plt.xlabel("Method")
plt.ylabel("Average Latency (ms)")

plt.title(
    "Average Service Latency"
)

plt.tight_layout()

plt.savefig(
    f"{output_folder}/average_latency.png",
    dpi=300
)

plt.close()


# -----------------------------------------
# Graph 3: Reliability
# -----------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    methods,
    reliability
)

plt.xlabel("Method")
plt.ylabel("Reliability")

plt.title(
    "Average Service Reliability"
)

plt.ylim(0.85, 0.92)

plt.tight_layout()

plt.savefig(
    f"{output_folder}/reliability.png",
    dpi=300
)

plt.close()


print("\nGraphs generated successfully!")

print(
    f"Saved in: {output_folder}/"
)

print("1. placement_success_rate.png")
print("2. average_latency.png")
print("3. reliability.png")