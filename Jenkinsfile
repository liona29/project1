pipeline {

    agent {label 'jenkins-slave' }
    parameters {
        string(name: 'IMAGANAME', defaultValue: 'bigchar', descriptrion: 'name for bilding image (flask bigchar web app)')
    }
    stages{
        stage("build") {
            steps{
                sh "docker build -t ${IMAGANAME} flaskbigapp:1"
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