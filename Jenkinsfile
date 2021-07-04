pipeline{
    agent {any}
    stages {
        stage ('checkout'){
            steps{
                checkout scm
            }
        }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
    }
}