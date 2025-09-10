# CI/CD Mini Project 🚀

This project demonstrates a **CI/CD pipeline with Jenkins, Docker, and Docker Compose**.  
It automatically builds a Docker image, pushes it to Docker Hub, and deploys it using Docker Compose.  

---

## 📂 Project Structure

```
ci-cd-mini-project/
│── app/                 # Application source code
│── docker-compose.yml   # Docker Compose file for deployment
│── Jenkinsfile          # Jenkins pipeline definition
│── .env                 # Environment variables (not committed)
```

---

## ⚙️ Features

- **Jenkins Pipeline** for CI/CD  
- **Docker Build & Push** to Docker Hub  
- **Automated Deployment** with Docker Compose  
- **Email Notifications** on pipeline success/failure  

---

## 🐳 Docker Compose Setup

The application is deployed with Docker Compose.

**docker-compose.yml** (key parts):
```yaml
services:
  web:
    image: yateshingale/myapp:latest
    ports:
      - "${APP_PORT}:5000"
    restart: always
    env_file:
      - .env
```

### Example `.env` file:
```env
APP_PORT=5000
APP_ENV=production
APP_SECRET=my-secret-key
```

Run the stack:
```bash
docker-compose up -d
```

Stop the stack:
```bash
docker-compose down
```

---

## 🔄 Jenkins Pipeline

The **Jenkinsfile** includes the following stages:

1. **Checkout** → Clones the repository  
2. **Build Docker Image** → Builds the app image  
3. **Push to Docker Hub** → Uploads the image to Docker Hub  
4. **Deploy with Docker Compose** → Runs containers on the server  

### Notifications
- **Success** → Sends ✅ success email  
- **Failure** → Sends ❌ failure email  

---

## 📧 Email Notifications Setup

This pipeline uses Jenkins **Email Extension Plugin (`emailext`)**.  
To configure:  

1. Install the plugin in Jenkins  
2. Configure SMTP in **Manage Jenkins → Configure System**  
3. Add your email (already set to `vickyingale2000@gmail.com`)  
4. Run the pipeline to test  

---

## ▶️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/yateshingale/ci-cd-mini-project.git
   cd ci-cd-mini-project
   ```

2. Create a `.env` file with your environment variables  

3. Run Jenkins pipeline → It will build, push, and deploy automatically  

---

## ✅ Requirements

- Docker & Docker Compose  
- Jenkins with required plugins:  
  - **Pipeline**  
  - **Email Extension**  
  - **Docker Pipeline**  

---

## 📌 Author

👤 **Yatesh Ingale**  
📧 [vickyingale2000@gmail.com](mailto:vickyingale2000@gmail.com)  
