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
                python3 -m venv $VENV_DIR
                source $VENV_DIR/bin/activate
                pip install --upgrade pip
                if [ -f requirements.txt ]; then
                    pip install -r requirements.txt
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
                source $VENV_DIR/bin/activate
                if [ -d tests ]; then
                    python -m unittest discover tests
                else
                    echo "No tests folder found, skipping tests."
                fi
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh '''
                source $VENV_DIR/bin/activate
                # Example: Run your app or copy files to server
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
