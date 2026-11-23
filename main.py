from src.service_generator import generate_services
from src.cloudlet_generator import generate_cloudlets
from src.baseline import place_service


def main():

    print("=" * 60)
    print("AIoT SERVICE PLACEMENT SIMULATION")
    print("=" * 60)

    # ------------------------------------------------
    # Generate service requests
    # ------------------------------------------------

    services = generate_services(
        num_services=20,
        seed=42
    )

    # ------------------------------------------------
    # Generate cloudlets
    # ------------------------------------------------

    cloudlets = generate_cloudlets(
        num_cloudlets=5,
        seed=42
    )

    # ------------------------------------------------
    # Display services
    # ------------------------------------------------

    print("\nSERVICES")
    print("-" * 60)

    print(services.to_string(index=False))

    # ------------------------------------------------
    # Display cloudlets
    # ------------------------------------------------

    print("\nCLOUDLETS")
    print("-" * 60)

    print(cloudlets.to_string(index=False))

    # ------------------------------------------------
    # Service placement
    # ------------------------------------------------

    print("\nSERVICE PLACEMENT")
    print("-" * 60)

    for _, service in services.iterrows():

        cloudlet_id = place_service(
            service,
            cloudlets
        )

        print(
            f"Service {service['service_id']} "
            f"({service['service_type']}) "
            f"-> Cloudlet {cloudlet_id}"
        )


if __name__ == "__main__":
    main()