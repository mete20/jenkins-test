pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh 'python3 -m venv venv' // Create a virtual environment
                sh './venv/bin/pip install --upgrade pip' // Upgrade pip
                sh './venv/bin/pip install -r requirements.txt' // Install dependencies
            }
        }

        stage('Test') {
            steps {
                sh './venv/bin/python -m unittest discover' // Run tests
            }
        }

        stage('Build') {
            steps {
                sh './venv/bin/python hello.py' // Execute the Python script
            }
        }
    }

    post {
        always {
            sh 'rm -rf venv' // Clean up virtual environment
        }
    }
}
