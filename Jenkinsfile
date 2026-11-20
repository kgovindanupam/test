pipeline {
    agent any

    parameters{
	string (
	 name: 'testing',
	 defaultValue: 'testing application',
	 description: 'Enter app name'
	    )
	}



stages {

stage('Display InPut'){
step{

echo '${params.name}'

}}}

}


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
                //bat 'python -m py_compile test_app.py'
                //bat 'python -m py_compile test.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing Python application'
                bat 'python test.py > output.txt'
                bat 'findstr /C:"444 Y" output.txt'
            }
        }

        stage('Deploy') {
            steps {
                //bat 'start "Python Web App" /B python test_app.py'
                echo 'Deploying Python application'
                //echo 't'
                echo 'G1'
                //bat 'python test.py'
            }
        }
    }




}

*/