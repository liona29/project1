pipeline {

    agent {label 'jenkins-slave' }

    stages{
        stage("build") {
            steps{
                sh "echo hello ari"
                sh "docker build -t bigchar flaskbigapp:1"             
                }
            }

        stage("up-to-ecr") {

            steps {
                sh "docker tag bigchar:latest 295862277960.dkr.ecr.eu-central-1.amazonaws.com/ariwein:latest${BUILD_NUMBER}"
                sh "aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 295862277960.dkr.ecr.eu-central-1.amazonaws.com"
                sh "docker push 295862277960.dkr.ecr.eu-central-1.amazonaws.com/ariwein:latest${BUILD_NUMBER}"
            }
        }

        stage("build helm") {

            steps {
                // sh "cd .."
                // sh "cd ./helmbigcharapp:1/chart"
                sh "sudo helm upgrade --install bigchar ./helmbigcharapp:1/chart --set containers.imageTag=latest${BUILD_NUMBER}"
            }
 
        }
        stage("deploy") {
            steps {
                sh "kubectl get ing big-char"
            }

        }
    }
}