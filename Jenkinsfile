pipeline {
    agent any

    stages {
        stage('Check Python') {
            steps {
                script {
                    sh 'python3 --version'
                }
            }
        }
        stage('Setup') {
            steps {
                script {
                    echo 'Setting up the environment'
                    sh 'python -m venv venv'
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing dependencies'
                    sh './venv/bin/pip install -r requirements.txt'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    echo 'Running tests'
                    sh './venv/bin/pytest'
                }
            }
        }
    }
}
