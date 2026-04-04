pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'sudhirsundriyal/calculator-app:latest'
        K8S_CONTEXT = 'kind-calculator'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/sudhirsundriyal/calculator-app.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                ./venv/bin/pip install --upgrade pip
                if [ -f requirements.txt ]; then
                    ./venv/bin/pip install -r requirements.txt
                fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                if [ -d tests ]; then
                    ./venv/bin/python -m unittest discover tests
                fi
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker push sudhirsundriyal/calculator-app:latest
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh """
                kubectl --context ${K8S_CONTEXT} apply -f k8s/deployment.yaml
                kubectl --context ${K8S_CONTEXT} apply -f k8s/service.yaml
                """
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
