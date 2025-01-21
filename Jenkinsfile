pipeline {
    agent any
    environment {
        SONARQUBE_SERVER = 'NPY'  // Nombre del servidor SonarQube configurado en Jenkins
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Clonando el repositorio...'
                git branch: 'main', url: 'https://github.com/Naty03Riveros/DeVOsTest.git'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                script {
                    echo 'Iniciando el análisis con SonarQube...'
                    withSonarQubeEnv('NPY') {  // Nombre del servidor SonarQube
                        sh 'sonar-scanner -Dsonar.projectKey=DeVOsTest -Dsonar.sources=./ -Dsonar.host.url=$SONAR_HOST_URL -Dsonar.login=$SONAR_AUTH_TOKEN'
                    }
                }
            }
        }
        stage('Wait for Quality Gate') {
            steps {
                script {
                    echo 'Esperando la verificación de la calidad...'
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline finalizado.'
        }
        success {
            echo 'Análisis completado con éxito.'
        }
        failure {
            echo 'Hubo errores en el análisis.'
        }
    }
}
