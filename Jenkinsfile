pipeline {
    agent any

    stages {

/*        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub'
                checkout scm
            }
        }
*/
        stage('Build') {
            steps {
                echo 'Building Python application'
                /*bat 'python -m py_compile test_app.py'
                bat 'python -m py_compile test.py'*/
            }
        }

        stage('Test') {
            steps {
                echo 'Testing Python application'
                /*bat 'python test.py > output.txt'
                bat 'findstr /C:"444 Y" output.txt'*/
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Python web application'
                //bat 'start "Python Web App" /B python test_app.py'
                echo 'Deploying Python application'
                //bat 'python test.py'
            }
        }
    }
}
