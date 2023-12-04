pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from your version control system (e.g., Git)
                git 'https://github.com/YaroslavPanasiuk/testcicd.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python dependencies using a virtual environment
                sh 'python -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run your Python tests
                sh 'source venv/bin/activate && python -m unittest discover tests'
            }
        }

        stage('Deploy') {
            steps {
                // Your deployment steps go here
                // For example, deploy to a server or cloud platform
                sh 'echo "Deploying the application..."'
            }
        }
    }
}
