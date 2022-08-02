pipeline {

    agent {label 'jenkins-slave' }

    stages{
        stage("build") {
            steps{
                sh "docker build -t jenkins ./flaskbigapp:1"
                }
            }

        stage("test") {

            steps {
                echo "testing ther application"
            }
        }

        stage("deploy") {

            steps {
                echo "deploying the application"
            }
        }
    }
}