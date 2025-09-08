pipeline {
    agent any

    environment {
        IMAGE_NAME = "yateshingale/myapp"
    }

    stages {

        // Stage 1: Checkout the repository
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/yateshingale/ci-cd-mini-project.git'
            }
        }

        // Stage 2: Build Docker Image
        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image: ${IMAGE_NAME}:latest"
                    sh 'docker build -t $IMAGE_NAME:latest ./app'
                }
            }
        }

        // Stage 3: Push Docker Image to Docker Hub
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-username', 
                    usernameVariable: 'DOCKER_HUB_USER', 
                    passwordVariable: 'DOCKER_HUB_PASS')]) {

                    echo "Logging into Docker Hub..."
                    sh 'echo $DOCKER_HUB_PASS | docker login -u $DOCKER_HUB_USER --password-stdin'

                    echo "Pushing Docker image..."
                    sh 'docker push $IMAGE_NAME:latest'
                }
            }
        }

        // Stage 4: Deploy with Docker Compose
        stage('Deploy with Docker Compose') {
            steps {
                script {
                    echo "Deploying application using Docker Compose..."
                    sh 'cd app && docker-compose down && docker-compose up -d'
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs for details."
        }
    }
}

