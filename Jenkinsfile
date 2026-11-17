pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building Python application'
                bat 'py -m py_compile test.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing Python application'
                bat 'py test.py > output.txt'
                bat 'findstr /C:"444 Y" output.txt'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Python application'
                bat 'py test.py'
            }
        }
    }
}