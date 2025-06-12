at Jenkinsfile 
pipeline {
  agent any

  stages {

    stage('Clone Code') {
      steps {
        echo 'Cloning from GitHub...'
        // Jenkins does this automatically
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          dockerImage = docker.build('flask-todo-app')
        }
      }
    }

    stage('Run Docker Compose') {
      steps {
        sh 'docker-compose up -d'
      }
    }
  }
}           
