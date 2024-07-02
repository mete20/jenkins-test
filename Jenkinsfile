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
        stage('Install venv') {
            steps{
                script {
                    echo 'Setting up the environment'
                    sh '''
                        sudo rm -rf /var/lib/apt/lists/*
                        sudo apt-get update
                        python3 -m venv venv
                        . venv/bin/activate
                    '''
                }
            }
        }

        stage('Setup') {
            steps {
                script {
                    echo 'Setting up the environment'
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
                        . venv/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    echo 'Running tests'
                    sh '''
                        . venv/bin/activate
                        pytest
                    '''
                }
            }
        }
    }
}
