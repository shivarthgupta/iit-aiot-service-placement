def calculate_latency(service, cloudlet):

    processing_latency = (
        service["cpu_required"] /
        cloudlet["total_cpu"]
    ) * 100

    network_latency = cloudlet["network_delay"]

    total_latency = (
        processing_latency +
        network_latency
    )

    return round(total_latency, 2)