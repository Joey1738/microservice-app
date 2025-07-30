import yaml

def generate_deployment_config(app_name, image, replicas, container_port):
    deployment = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {
            "name": f"{app_name}-deployment"
        },
        "spec": {
            "replicas": replicas,
            "selector": {
                "matchLabels": {
                    "app": app_name
                }
            },
            "template": {
                "metadata": {
                    "labels": {
                        "app": app_name
                    }
                },
                "spec": {
                    "containers": [
                        {
                            "name": app_name,
                            "image": image,
                            "ports": [
                                {
                                    "containerPort": container_port
                                }
                            ]
                        }
                    ]
                }
            }
        }
    }
    return deployment

def save_yaml(data, filename):
    with open(filename, 'w') as f:
        yaml.dump(data, f, sort_keys=False)
    print(f"✅ Generated file saved as {filename}")

if __name__ == "__main__":
    # Customize your deployment parameters here:
    app_name = "backend"
    image = "joeyomagwu1738/backend:latest"
    replicas = 2
    container_port = 5001

    deployment_yaml = generate_deployment_config(app_name, image, replicas, container_port)
    save_yaml(deployment_yaml, "backend-deployment.yaml")
