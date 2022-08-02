pipeline {

    agent any

    stages{
        stage("build") {
            steps{
                sh "docker build flaskbigapp:1"
                }
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
