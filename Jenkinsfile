pipeline {
  agent any

  stages {
    stage('Clone Code') {
      steps {
        echo 'Cloning code from GitHub...'
        // No actual git step needed — Jenkins does it automatically
      }
    }

    stage('Lint Python Code') {
    steps {
        sh 'python -m py_compile calc.py'
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
