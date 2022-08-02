pipeline {

    agent {label 'jenkins-slave' }
    parameters {
        string(name: 'IMAGANAME', defaultValue: 'bigchar', description: 'name for bilding image (flask bigchar web app)')
    }
    stages{
        stage("build") {
            steps{
                sh "docker build -t ${params.IMAGANAME} flaskbigapp:1"
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