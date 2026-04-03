pipeline {
    agent any

    environment {
        WORK_DIR = "${env.WORKSPACE}"
        VENV_DIR = "${env.WORKSPACE}/venv"
        PYTHON = "${env.WORKSPACE}/venv/bin/python"
        PIP = "${env.WORKSPACE}/venv/bin/pip"
    }

    stages {
        stage('Workspace Info') {
            steps {
                echo "Workspace: ${WORK_DIR}"
                sh 'pwd'
                sh 'ls -la'
            }
        }

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
                python3 -m venv $VENV_DIR
                $PIP install --upgrade pip
                if [ -f requirements.txt ]; then
                    $PIP install -r requirements.txt
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
                if [ -d tests ]; then
                    $PYTHON -m unittest discover tests
                else
                    echo "No tests folder found, skipping tests."
                fi
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application (simulation)...'
                sh '''
                # Example: Run your app or copy files to server
                echo "Application deployed successfully"
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
