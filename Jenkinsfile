pipeline {
    agent any

    environment {
        VIRTUAL_ENV = "${WORKSPACE}/venv"
    }

    stages {
        stage('Setup Python Environment') {
            steps {
                // Install virtualenv
                sh '/Users/metehan.yaka/Dev/jenkins-test/venv/bin/python3 -m venv venv'
                // Activate virtualenv and install dependencies
                sh '. ${VIRTUAL_ENV}/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh '. ${VIRTUAL_ENV}/bin/activate && flake8 .'
            }
        }

        stage('Test') {
            steps {
                sh '. ${VIRTUAL_ENV}/bin/activate && pytest'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 app.py'
            }
        }

        stage('Package') {
            steps {
                sh 'tar -czf python_app.tar.gz app.py'
            }
        }

        stage('Deploy') {
            steps {
                // Dummy deploy step
                sh 'echo "Deploying application..."'
                // You can add real deployment commands here
            }
        }
    }

    post {
        always {
            // Clean up virtual environment
            sh 'rm -rf venv'
        }
    }
}
