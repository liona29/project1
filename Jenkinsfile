pipeline {

    agent {label 'jenkins-slave' }
    parameters {
        string(name: 'IMAGANAME', defaultValue: 'bigchar', description: 'name for bilding image (flask bigchar web app)')
    }
    stages{
        stage("build") {
            steps{
                sh "docker build -t 295862277960.dkr.ecr.eu-central-1.amazonaws.com/ariwein:${params.IMAGANAME} flaskbigapp:1"
                
                }
            }

        stage("up-to-ecr") {

            steps {
                sh "docker push 295862277960.dkr.ecr.eu-central-1.amazonaws.com/ariwein:${params.IMAGANAME}"
            }
        }

        stage("down-from-ecr") {

            steps {
                sh "docker rmi 295862277960.dkr.ecr.eu-central-1.amazonaws.com/ariwein:${params.IMAGANAME}"
                sh "docker run 295862277960.dkr.ecr.eu-central-1.amazonaws.com/ariwein:${params.IMAGANAME}"
            }
        }
    }
}