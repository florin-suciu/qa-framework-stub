import yaml
import os


def load_environment():
    # Get the absolute path to the environment.yaml file
    environment_path = os.path.join(
        os.path.dirname(__file__), "../config/environment.yaml"
    )

    # Load the environment configuration from the YAML file
    with open(environment_path, "r") as file:
        environment = yaml.safe_load(file)

    return environment
