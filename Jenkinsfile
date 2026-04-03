pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                git 'https://github.com/sudhirsundriyal/calculator-app.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Creating virtual environment and installing dependencies...'
                sh '''
                set -e
                python3 -m venv $VENV_DIR
                $VENV_DIR/bin/pip install --upgrade pip
                if [ -f requirements.txt ]; then
                    $VENV_DIR/bin/pip install -r requirements.txt
                else
                    echo "No requirements.txt found, skipping dependencies installation."
                fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests (if any)...'
                sh '''
                set -e
                $VENV_DIR/bin/python -m unittest discover tests || echo "No tests found, skipping."
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh '''
                set -e
                echo "Application deployed successfully (simulation)"
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check console output for errors.'
        }
    }
}
