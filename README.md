# **DevOps Learning Summary - Calculator App Project**

## **1. Project Overview**
- This project is a **Calculator web application** built using **Python (Flask)** and **Docker**.  
- It demonstrates a **full DevOps workflow**, from code to deployment on a **Kubernetes cluster** using **Jenkins CI/CD**.

---

## **2. Features Learned**
- Simple **web-based calculator** interface.  
- **Docker containerization** and image management.  
- **Kubernetes deployment** using YAML configuration files.  
- **Automated CI/CD pipeline** with Jenkins for build, test, and deployment.  

---

## **3. Tech Stack**
- **Python 3.9**  
- **Flask** (web framework)  
- **Docker** (containerization)  
- **Kubernetes (Minikube)** (container orchestration)  
- **Jenkins** (CI/CD automation)  

---

## **4. Key Commands & Usage**

### **Linux Basics**
- `ls` → List files and folders  
- `cd <folder>` → Change directory  
- `pwd` → Print current working directory  
- `mkdir <folder>` → Create a new directory  
- `chmod 400 <file>` → Secure private key file permissions  

### **Git**
- `git clone <repo_url>` → Clone a project repository  
- `git branch` → List branches  
- `git checkout <branch>` → Switch branches  
- `git pull` → Fetch and merge latest changes  

### **Python**
- `python3 -m venv venv` → Create virtual environment  
- `source venv/bin/activate` → Activate virtual environment  
- `pip install -r requirements.txt` → Install dependencies  
- `python -m unittest discover tests` → Run unit tests  

### **Docker**
- `docker build -t <image_name> .` → Build Docker image  
- `docker login` → Authenticate with Docker Hub  
- `docker push <image_name>` → Push Docker image to Docker Hub  
- `docker ps` → List running containers  

### **Kubernetes**
- `kubectl apply -f <file>` → Deploy resources to cluster  
- `kubectl get pods` → Check pod status  
- `kubectl get svc` → Check service status  

### **Jenkins / CI-CD**
- Jenkinsfile automates the following:  
  1. **Git checkout**  
  2. **Python environment setup**  
  3. **Run unit tests**  
  4. **Build Docker image**  
  5. **Push Docker image to Docker Hub**  
  6. **Deploy to Kubernetes**  

---

## **5. Step-wise Project Implementation**
1. **Cloned repository** and pushed Jenkinsfile to GitHub.  
2. **Set up Python virtual environment** and installed dependencies.  
3. **Ran unit tests** to ensure all tests passed.  
4. **Built Docker image** and pushed it to Docker Hub.  
5. **Applied Kubernetes deployment and service YAML** files and verified pods.  
6. **Automated the workflow** using Jenkins CI/CD pipeline.  

---

## **6. Key Learnings**
- Linux command-line basics and file permissions.  
- Git version control workflow.  
- Python virtual environment and package management.  
- Docker image build, tagging, and push process.  
- Kubernetes basics, including YAML configuration and deployment commands.  
- Jenkins declarative pipeline structure and automation.  

---

## **7. Next Steps for Zero-to-Hero**
- AWS services: EC2, S3, VPC, IAM - deploy and manage.  
- Advanced Kubernetes: ingress, configmaps, secrets, persistent volumes.  
- CI/CD: multi-branch pipelines and testing strategies.  
- Infrastructure as Code (IaC) tools: Terraform, CloudFormation.  
- Logging & Monitoring: Prometheus, Grafana.  

---

## **Author**
**Sudhir Sundriyal**  

*This summary is aimed at beginners starting a career in DevOps.*
