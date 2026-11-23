from src.latency import calculate_latency
from src.reliability import calculate_reliability


def place_service(service, cloudlets):

    best_cloudlet_index = None
    best_score = float("-inf")

    for index, cloudlet in cloudlets.iterrows():

        # Check CPU availability
        if cloudlet["available_cpu"] < service["cpu_required"]:
            continue

        # Check memory availability
        if cloudlet["available_memory"] < service["memory_required"]:
            continue

        # Calculate latency
        latency = calculate_latency(
            service,
            cloudlet
        )

        # Calculate reliability
        reliability = calculate_reliability(
            cloudlet
        )

        # Check latency requirement
        if latency > service["latency_requirement"]:
            continue

        # Lower latency = better
        latency_score = 1 / (1 + latency)

        # Combined score
        score = (
            0.5 * reliability +
            0.5 * latency_score
        )

        if score > best_score:

            best_score = score
            best_cloudlet_index = index

    # No suitable cloudlet found
    if best_cloudlet_index is None:
        return None

    # Reserve CPU resources
    cloudlets.at[
        best_cloudlet_index,
        "available_cpu"
    ] -= service["cpu_required"]

    # Reserve memory resources
    cloudlets.at[
        best_cloudlet_index,
        "available_memory"
    ] -= service["memory_required"]

    # Return cloudlet ID
    return int(
        cloudlets.at[
            best_cloudlet_index,
            "cloudlet_id"
        ]
    )