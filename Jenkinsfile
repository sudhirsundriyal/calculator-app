pipeline {
    agent any

    parameters {
        string(name: 'NUM1', defaultValue: '10', description: 'First number')
        string(name: 'NUM2', defaultValue: '20', description: 'Second number')
    }

    environment {
        VENV_DIR = "${env.WORKSPACE}/venv"
        PYTHON = "${env.WORKSPACE}/venv/bin/python"
        PIP = "${env.WORKSPACE}/venv/bin/pip"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/sudhirsundriyal/calculator-app.git',
                    credentialsId: 'github-token'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv $VENV_DIR
                $PIP install --upgrade pip
                if [ -f requirements.txt ]; then
                    $PIP install -r requirements.txt
                fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                if [ -d tests ]; then
                    $PYTHON -m unittest discover tests
                fi
                '''
            }
        }

        stage('Run App') {
            steps {
                sh '''
                NUM1=${NUM1:-10}
                NUM2=${NUM2:-20}
                $PYTHON app.py $NUM1 $NUM2
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application (simulation)...'
            }
        }
    } // end stages

    post {
        success {
            echo 'Pipeline completed successfully!'
            // slackSend channel: '#devops', message: 'Build Successful'
        }
        failure {
            echo 'Pipeline failed.'
            // slackSend channel: '#devops', message: 'Build Failed'
        }
    } // end post
} // end pipeline
