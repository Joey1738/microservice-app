# Microservices Project

A complete microservices-based project using Flask (backend/frontend), deployed via Docker, Kubernetes, and Terraform, with automation using Ansible and CI/CD using GitHub Actions.

---

## Project Structure

microservices-project/
├── backend/ # Flask backend service
├── frontend/ # Flask frontend service
├── k8s/ # Kubernetes manifests (deployments, services, ingress)
├── terraform/ # Terraform code to provision Kubernetes infra
├── ansible-dockers-k8s/ # Ansible playbooks to install Docker, K8s
├── python_utilities/ # Python helper scripts
├── .github/ # GitHub Actions CI/CD workflows
├── docker_compose.yml # Docker Compose config (optional for local test)
├── generate_deploment.py # Script to auto-generate deployment YAML
├── local-microservice.crt # Local SSL certificate for HTTPS (optional)
├── endpoint_test.log # Log file for API tests
├── app.log # Application logs
├── .gitignore
├── .gitattributes
├── vim_host
└── README.md

markdown
Copy
Edit

---

## Requirements

Install the following tools:

- [Docker](https://www.docker.com/)
- [Python 3.10+](https://www.python.org/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [minikube](https://minikube.sigs.k8s.io/docs/)
- [Terraform](https://developer.hashicorp.com/terraform/install)
- [Ansible](https://docs.ansible.com/)
- [Git](https://git-scm.com/)

---

## How to Run the Project

### Option 1: Run Locally with Docker Compose

```bash
docker-compose -f docker_compose.yml up --build
Option 2: Deploy with Kubernetes
bash
Copy
Edit
minikube start           # Start local Kubernetes cluster
kubectl apply -f k8s/    # Apply all Kubernetes manifests
Option 3: Provision Infrastructure with Terraform
bash
Copy
Edit
cd terraform/
terraform init
terraform apply
Option 4: Automate Setup with Ansible
bash
Copy
Edit
cd ansible-dockers-k8s/
ansible-playbook playbook.yml
This installs Docker, Kubelet, Kubectl, and optionally initializes the Kubernetes cluster.

Run API Endpoint Tests
bash
Copy
Edit
python3 python_utilities/test_endpoints.py
Logs will be saved in endpoint_test.log.

SSL Certificate
If you're using HTTPS locally:

local-microservice.crt is your local certificate.

Make sure your Ingress or frontend is configured to use it.

GitHub Actions CI/CD
All workflows are stored under .github/workflows/.

CI runs on pull requests and pushes to the main or dev branch.

Logs
app.log – backend application log file.

endpoint_test.log – API test results log file.

Author
Joey Omagwu
GitHub Profile