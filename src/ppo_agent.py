from stable_baselines3 import PPO

from src.environment import ServicePlacementEnv


def create_environment():

    env = ServicePlacementEnv(
        num_services=20,
        num_cloudlets=5,
        seed=42
    )

    return env


def train_ppo():

    # Create environment
    env = create_environment()

    # Create PPO model
    model = PPO(
        policy="MlpPolicy",
        env=env,
        learning_rate=0.0003,
        n_steps=256,
        batch_size=64,
        n_epochs=10,
        gamma=0.99,
        verbose=1
    )

    print("\nStarting PPO training...\n")

    # Train
    model.learn(
        total_timesteps=10000
    )

    # Save model
    model.save(
        "results/ppo_service_placement"
    )

    print("\nPPO training completed!")

    print(
        "Model saved to: "
        "results/ppo_service_placement.zip"
    )

    return model


if __name__ == "__main__":

    train_ppo()