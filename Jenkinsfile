pipeline {
    agent any

    environment {
        PYENV_ROOT = sh(script: 'echo $HOME/.pyenv', returnStdout: true).trim()
        PATH = "$PYENV_ROOT/bin:$PATH"
    }

    stages {
        stage('Check Python') {
            steps {
                script {
                    sh 'python --version'
                }
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                script {
                    echo 'Setting up the virtual environment'
                    sh '''
                        pyenv install 3.11.2
                        pyenv virtualenv 3.11.2 my-python-env
                        pyenv activate my-python-env
                    '''
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing dependencies'
                    sh 'pip install --upgrade pip'
                    sh 'pip install -r requirements.txt'
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
                    sh 'pyenv deactivate'
                }
            }
        }
    }
}
