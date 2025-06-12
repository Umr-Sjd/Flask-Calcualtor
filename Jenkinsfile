pipeline{
    agent any

    stages{
            stage('Clone Code'){
                steps{
                    script
                        echo 'cloning the code ....'
            
                }
        
             }
            stage('docker build'){
                steps{
                    script{
                        dockerImage = docker.build('my-calc-app')
                    }
                }
            }
            stage{
                steps{
                    sh 'docker compose up -d'
                }
            }

    }

}