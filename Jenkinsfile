pipeline {
    agent any

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
        source $VENV_DIR/bin/activate
        python3 app.py  # अब default values use होंगी
        '''
    }
}    

        stage('Deploy') {
            steps {
                echo 'Deploying application (simulation)...'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
