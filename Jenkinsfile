pipeline {
    agent any

    environment {
        // Define environment variables here if needed
        VIRTUAL_ENV = 'venv'  // Define the virtual environment directory
        PATH = "${env.VIRTUAL_ENV}/bin:$PATH"  // Add virtual environment binaries to PATH
    }

    stages {
        stage('Check Python') {
            steps {
                script {
                    sh 'python3 --version'
                }
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                script {
                    echo 'Setting up the virtual environment'
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                    '''
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing dependencies'
                    sh '''
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    echo 'Running tests'
                    sh 'pytest'
                }
            }
        }
        stage('Deactivate Virtual Environment') {
            steps {
                script {
                    echo 'Deactivating virtual environment'
                    sh 'deactivate || true'
                }
            }
        }
    }
}
