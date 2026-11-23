import numpy as np
import pandas as pd


def generate_cloudlets(num_cloudlets=5, seed=42):

    np.random.seed(seed)

    cloudlets = []

    for cloudlet_id in range(num_cloudlets):

        total_cpu = np.random.randint(10, 21)
        total_memory = np.random.randint(16, 33)

        reliability = round(
            np.random.uniform(0.80, 0.99),
            3
        )

        network_delay = round(
            np.random.uniform(5, 30),
            2
        )

        cloudlet = {
            "cloudlet_id": cloudlet_id,
            "total_cpu": total_cpu,
            "total_memory": total_memory,
            "available_cpu": total_cpu,
            "available_memory": total_memory,
            "reliability": reliability,
            "network_delay": network_delay
        }

        cloudlets.append(cloudlet)

    return pd.DataFrame(cloudlets)


if __name__ == "__main__":

    cloudlets = generate_cloudlets(5)

    print("\nGenerated Cloudlets:")
    print(cloudlets)