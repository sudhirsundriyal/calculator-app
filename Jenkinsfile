pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/sudhirsundriyal/calculator-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                ./venv/bin/pip install --upgrade pip

                if [ -f requirements.txt ]; then
                    ./venv/bin/pip install -r requirements.txt
                else
                    echo "No requirements.txt"
                fi
                '''
            }
        }

        stage('Run App') {
            steps {
                sh '''
                echo "Running app..."
                '''
            }
        }
    }
}
