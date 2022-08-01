pipeline {

    agent any

    stages{
        stage("build") {
            steps{
                echo "========executing A========"
            }
        }

        stage("test") {

            step {
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