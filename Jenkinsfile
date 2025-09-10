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
            echo "✅ Pipeline completed successfully!"
            emailext (
                subject: "✅ SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """
                <p>Good news! Your Jenkins pipeline completed successfully 🎉</p>
                <p><b>Job:</b> ${env.JOB_NAME}</p>
                <p><b>Build Number:</b> ${env.BUILD_NUMBER}</p>
                <p><b>Build URL:</b> <a href='${env.BUILD_URL}'>Click Here</a></p>
                """,
                to: "vickyingale2000@gmail.com"
            )
        }
        failure {
            echo "❌ Pipeline failed. Check logs for details."
            emailext (
                subject: "❌ FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """
                <p>Unfortunately, your Jenkins pipeline failed ⚠️</p>
                <p><b>Job:</b> ${env.JOB_NAME}</p>
                <p><b>Build Number:</b> ${env.BUILD_NUMBER}</p>
                <p><b>Build URL:</b> <a href='${env.BUILD_URL}'>Click Here</a></p>
                """,
                to: "vickyingale2000@gmail.com"
            )
        }
    }
}