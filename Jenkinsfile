pipeline {
  agent any
    stages {
      stage('setup') {
          steps {
            sh 'pip install pytest'
            sh 'pip install selenium'
        }
      }
      stage('test') {
        steps {
          sh 'python3 -m pytest'
        }
      }
    }
  }
