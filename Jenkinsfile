pipeline {
    agent any
    environment {
        DOCKER_HUB_USER = credentials('dockerhub-username')
        DOCKER_HUB_PASS = credentials('dockerhub-username') // same ID
        IMAGE_NAME = "yateshingale/myapp"
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yateshingale/ci-cd-mini-project.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest ./app'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                sh 'echo $DOCKER_HUB_PASS | docker login -u $DOCKER_HUB_USER --password-stdin'
                sh 'docker push $IMAGE_NAME:latest'
            }
        }
        stage('Deploy with Docker Compose') {
            steps {
                sh 'docker-compose down && docker-compose up -d'
            }
        }
    }
}
