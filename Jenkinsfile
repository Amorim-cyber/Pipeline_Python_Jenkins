pipeline {
  agent any
    stages {
      stage('setup') {
          steps {
            sh 'pip install pytest'
            sh 'pip install selenium'
            sh 'pip install chromedriver-py'
        }
      }
      stage('test') {
        steps {
          sh 'python3 -m pytest'
        }
      }
    }
  }
