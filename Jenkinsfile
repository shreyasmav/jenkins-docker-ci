pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'shreyasmav'
        // “dockerhub-creds” is the ID of the Jenkins credentials you will create
        DOCKERHUB_CREDENTIALS = 'dockerhub-creds'
        IMAGE_NAME = 'shreyas-ci-demo'
    }

    // Trigger on every push (if GitHub integration is configured)
    triggers {
        githubPush()
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from the same Git repo that contains this Jenkinsfile
                checkout scm
            }
        }

        stage('Shreyas - Build Docker Image') {
            steps {
                script {
                    sh """
                      echo "Building Docker image..."
                      docker build -t ${DOCKERHUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER} .
                    """
                }
            }
        }

        stage('Shreyas - Login to Dockerhub') {
            steps {
                script {
                    withCredentials([usernamePassword(
                        credentialsId: DOCKERHUB_CREDENTIALS,
                        usernameVariable: 'DOCKERHUB_USERNAME',
                        passwordVariable: 'DOCKERHUB_PASSWORD'
                    )]) {
                        sh """
                          echo "Logging in to Docker Hub..."
                          echo "${DOCKERHUB_PASSWORD}" | docker login -u "${DOCKERHUB_USERNAME}" --password-stdin
                        """
                    }
                }
            }
        }

        stage('Shreyas - Push image to Dockerhub') {
            steps {
                script {
                    sh """
                      echo "Pushing Docker image to Docker Hub..."
                      docker push ${DOCKERHUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER}
                    """
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline finished successfully. Image pushed: ${DOCKERHUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER}"
        }
        failure {
            echo "Pipeline failed. Check the stage logs above."
        }
    }
}
