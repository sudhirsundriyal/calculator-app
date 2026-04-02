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
                sh 'pip install -r requirements.txt || echo "No requirements file found"'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "No tests defined"'
                // अगर tests folder है तो: sh 'python -m unittest discover tests'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying calculator-app..."'
            }
        }
    }
}
