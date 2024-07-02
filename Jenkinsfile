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
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing dependencies'
                    sh '''
                        pip3 install --user -r requirements.txt
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
    }
}
