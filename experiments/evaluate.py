from stable_baselines3 import PPO

from src.environment import ServicePlacementEnv


def evaluate_ppo(num_episodes=10):

    # Load trained PPO model
    model = PPO.load(
        "results/ppo_service_placement"
    )

    successful_placements = 0
    total_requests = 0

    total_latency = 0
    successful_latency_count = 0

    total_reliability = 0
    successful_reliability_count = 0

    print("\n")
    print("=" * 60)
    print("PPO EVALUATION")
    print("=" * 60)

    for episode in range(num_episodes):

        env = ServicePlacementEnv(
            num_services=20,
            num_cloudlets=5,
            seed=episode + 100
        )

        observation, info = env.reset()

        episode_success = 0

        while True:

            action, _ = model.predict(
                observation,
                deterministic=True
            )

            observation, reward, terminated, truncated, info = env.step(
                action
            )

            total_requests += 1
            print(
    f"Service {info['service_id']} "
    f"-> Cloudlet {info['cloudlet_id']} | "
    f"Latency: {info['latency']:.2f} ms | "
    f"Success: {info['success']}"
)

            if info["success"]:

                successful_placements += 1
                episode_success += 1

                total_latency += info["latency"]
                successful_latency_count += 1

                cloudlet_id = info["cloudlet_id"]

                cloudlet = env.cloudlets[
                    env.cloudlets["cloudlet_id"]
                    == cloudlet_id
                ].iloc[0]

                total_reliability += cloudlet[
                    "reliability"
                ]

                successful_reliability_count += 1

            if terminated or truncated:
                break

        print(
            f"Episode {episode + 1}: "
            f"{episode_success}/20 services placed"
        )

    # -----------------------------------------
    # Calculate metrics
    # -----------------------------------------

    placement_rate = (
        successful_placements /
        total_requests
    ) * 100

    if successful_latency_count > 0:

        average_latency = (
            total_latency /
            successful_latency_count
        )

    else:

        average_latency = 0

    if successful_reliability_count > 0:

        average_reliability = (
            total_reliability /
            successful_reliability_count
        )

    else:

        average_reliability = 0

    # -----------------------------------------
    # Results
    # -----------------------------------------

    print("\n")
    print("=" * 60)
    print("FINAL PPO RESULTS")
    print("=" * 60)

    print(
        f"Total Requests: {total_requests}"
    )

    print(
        f"Successful Placements: "
        f"{successful_placements}"
    )

    print(
        f"Placement Success Rate: "
        f"{placement_rate:.2f}%"
    )

    print(
        f"Average Latency: "
        f"{average_latency:.2f} ms"
    )

    print(
        f"Average Reliability: "
        f"{average_reliability:.4f}"
    )


if __name__ == "__main__":

    evaluate_ppo(
        num_episodes=10
    )