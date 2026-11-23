import numpy as np
import pandas as pd


SERVICE_TYPES = {
    "AR_VR": {
        "cpu": 4,
        "memory": 4,
        "latency_requirement": 50
    },

    "VIDEO_ANALYTICS": {
        "cpu": 6,
        "memory": 8,
        "latency_requirement": 100
    },

    "ONLINE_GAMING": {
        "cpu": 3,
        "memory": 4,
        "latency_requirement": 30
    },

    "IOT_MONITORING": {
        "cpu": 2,
        "memory": 2,
        "latency_requirement": 150
    }
}


def generate_services(num_services=20, seed=42):

    np.random.seed(seed)

    services = []

    service_names = list(SERVICE_TYPES.keys())

    for service_id in range(num_services):

        service_type = np.random.choice(service_names)

        requirements = SERVICE_TYPES[service_type]

        service = {
            "service_id": service_id,
            "service_type": service_type,
            "cpu_required": requirements["cpu"],
            "memory_required": requirements["memory"],
            "latency_requirement": requirements["latency_requirement"]
        }

        services.append(service)

    return pd.DataFrame(services)


if __name__ == "__main__":

    services = generate_services(20)

    print("\nGenerated Services:")
    print(services)

    print("\nService Distribution:")
    print(services["service_type"].value_counts())