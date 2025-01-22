pipeline {
    agent any
    environment {
        SONARQUBE_URL = 'http://test:9000' // Reemplazar con tu URL de SonarQube
        SONARQUBE_TOKEN = 'squ_3266dabd4f5d0edb2d8c41ae1ae5d4865280e593' // Reemplazar con tu token de SonarQube
    }
    stages {
        stage('Clonar Repositorio') {
            steps {
                echo 'Clonando el repositorio...'
                git url: 'https://github.com/Naty03Riveros/DeVOsTest.git', branch: 'main' // Usar la rama correcta
            }
        }
        stage('Análisis SonarQube') {
            steps {
                echo 'Ejecutando análisis con SonarQube...'
                sh '''
                    sonar-scanner \
                        -Dsonar.projectKey=DeVOsTest \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=$SONARQUBE_URL \
                        -Dsonar.login=$SONARQUBE_TOKEN
                '''
            }
        }
        stage('Probar') {
            steps {
                echo 'Ejecutando pruebas...'
                sh 'pytest'
            }
        }
        stage('Desplegar') {
            steps {
                echo 'Desplegando aplicación...'
                // Agrega tu lógica de despliegue aquí
            }
        }
    }
    post {
        failure {
            echo 'Hubo un error en el pipeline.'
        }
    }
}
