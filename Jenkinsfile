pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    git 'https://github.com/YaroslavPanasiuk/testcicd.git'
                }
            }
        }

        stage('Build and Test') {
            steps {
                script {
                    bat 'python -m venv venv'
                    bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
                    bat 'venv\\Scripts\\activate && python -m unittest discover tests'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    bat 'echo "Deploying the application..."'
                    // Add your deployment steps here
                }
            }
        }
    }
}
