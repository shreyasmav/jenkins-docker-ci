pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'shreyasmav'
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
                // generated pipeline script from Jenkins Pipeline Syntax
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/shreyasmav/jenkins-docker-ci']])
            }
        }

        stage('Shreyas - Build Docker Image') {
            steps {
                script {
                    bat """
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
                        bat """
                          echo Logging in to Docker Hub...
                          docker login -u %DOCKERHUB_USERNAME% -p %DOCKERHUB_PASSWORD%
                        """
                    }
                }
            }
        }

        stage('Shreyas - Push image to Dockerhub') {
            steps {
                script {
                    bat """
                      echo Pushing Docker image to Docker Hub...
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
