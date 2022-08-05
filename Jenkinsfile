pipeline {

    agent {label 'k8s-slave' }
    environment 
    parameters {
        string(name: 'IMAGANAME', defaultValue: 'bigchar', description: 'name for bilding image (flask bigchar web app)')
    }
    stages{
        stage("build") {
            steps{
                sh "echo hello ari"
                sh "cd flaskbigapp:1"
                sh "docker build -t bigchar ."             
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
                sh "cd .."
                sh "cd ./helmbigcharapp:1/chart"
                sh "helm upgrade --install bigchar . --set containers.imageTag=latest${BUILD_NUMBER}"
            }
 
        }
        stage("deploy") {
            steps {
                sh "kubectl get ing big-char"
            }

        }
    }
}