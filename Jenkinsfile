pipeline {
  agent any

  stages {
    stage('Clone Code') {
      steps {
        echo 'Cloning code from GitHub...'
        // No actual git step needed — Jenkins does it automatically
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          dockerImage = docker.build('flask-calc-app')
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
