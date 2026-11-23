from src.service_generator import generate_services
from src.cloudlet_generator import generate_cloudlets
from src.baseline import place_service
from src.latency import calculate_latency


def evaluate_baseline(num_episodes=10):

    total_requests = 0
    successful_placements = 0

    total_latency = 0
    latency_count = 0

    total_reliability = 0
    reliability_count = 0

    print("\n")
    print("=" * 60)
    print("BASELINE EVALUATION")
    print("=" * 60)

    for episode in range(num_episodes):

        # -----------------------------------------
        # Generate same type of workload
        # -----------------------------------------

        services = generate_services(
            num_services=20,
            seed=episode + 100
        )

        cloudlets = generate_cloudlets(
            num_cloudlets=5,
            seed=episode + 100
        )

        episode_success = 0

        # -----------------------------------------
        # Place each service
        # -----------------------------------------

        for _, service in services.iterrows():

            cloudlet_id = place_service(
                service,
                cloudlets
            )

            total_requests += 1

            # -------------------------------------
            # Successful placement
            # -------------------------------------

            if cloudlet_id is not None:

                successful_placements += 1
                episode_success += 1

                # Find selected cloudlet
                cloudlet = cloudlets[
                    cloudlets["cloudlet_id"]
                    == cloudlet_id
                ].iloc[0]

                # Calculate latency
                latency = calculate_latency(
                    service,
                    cloudlet
                )

                total_latency += latency
                latency_count += 1

                # Reliability
                total_reliability += (
                    cloudlet["reliability"]
                )

                reliability_count += 1

        print(
            f"Episode {episode + 1}: "
            f"{episode_success}/20 services placed"
        )

    # ---------------------------------------------
    # Calculate final metrics
    # ---------------------------------------------

    placement_success_rate = (
        successful_placements /
        total_requests
    ) * 100

    if latency_count > 0:

        average_latency = (
            total_latency /
            latency_count
        )

    else:

        average_latency = 0

    if reliability_count > 0:

        average_reliability = (
            total_reliability /
            reliability_count
        )

    else:

        average_reliability = 0

    # ---------------------------------------------
    # Print results
    # ---------------------------------------------

    print("\n")
    print("=" * 60)
    print("FINAL BASELINE RESULTS")
    print("=" * 60)

    print(
        f"Total Requests: "
        f"{total_requests}"
    )

    print(
        f"Successful Placements: "
        f"{successful_placements}"
    )

    print(
        f"Placement Success Rate: "
        f"{placement_success_rate:.2f}%"
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

    evaluate_baseline(
        num_episodes=10
    )