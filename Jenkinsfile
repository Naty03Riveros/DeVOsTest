pipeline {
    agent any

    environment {
        SONARQUBE = 'test'  // Nombre del servidor SonarQube configurado en Jenkins
    }

    stages {
        stage('Clonar Repositorio') {
            steps {
                echo 'Clonando el repositorio...'
                git branch: 'main', url: 'https://github.com/Naty03Riveros/DeVOsTest.git'
            }
        }

        stage('Preparar Entorno') {
            steps {
                echo 'Creando y activando entorno virtual...'
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                echo 'Instalando dependencias del proyecto...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Análisis SonarQube') {
            steps {
                script {
                    // Ejecutando el análisis con SonarQube
                    sh '''
                    source venv/bin/activate
                    sonar-scanner \
                    -Dsonar.projectKey=DeVOsTest \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=http://localhost:9000 \
                    -Dsonar.login=squ_3266dabd4f5d0edb2d8c41ae1ae5d4865280e593
                    '''
                }
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
                echo 'Desplegando la aplicación...'
                // Agrega aquí tus comandos de despliegue
            }
        }
    }

    post {
        success {
            echo '¡El pipeline fue exitoso!'
        }
        failure {
            echo 'Hubo un error en el pipeline.'
        }
    }
}
