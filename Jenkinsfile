pipeline {
    agent any

    environment {
        VENV = "myenv"
        PYTHON = "C:\\Users\\imran\\AppData\\Local\\Programs\\Python\\Python38\\python.exe"   // <-- adjust if Python path is different
        DOCKER_IMAGE = "imrandocker24/djredcledockerjenkins:latest"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/imranworkspace/DjRedCleDockerJenkins'
            }
        }

        stage('Setup Virtualenv') {
            steps {
                bat "%PYTHON% -m venv %VENV%"
                bat "%VENV%\\Scripts\\python -m pip install --upgrade pip"
                bat "%VENV%\\Scripts\\pip install -r requirnments.txt"
            }
        }

        stage('Run Migrations') {
            steps {
                bat "%VENV%\\Scripts\\python manage.py makemigrations"
                bat "%VENV%\\Scripts\\python manage.py migrate"
            }
        }

        stage('Run Tests') {
            steps {
                bat "%VENV%\\Scripts\\python manage.py test myapp.tests.test_views"
                bat "%VENV%\\Scripts\\python manage.py test myapp.tests.test_models"
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %DOCKER_IMAGE% ."
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat """
                        echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                        docker push %DOCKER_IMAGE%
                    """
                }
            }
        }


        stage('Deploy to Server') {
            steps {
                sshagent(['my-ssh-cred-id']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no deploy@myapp.example.com "
                          docker pull imrandocker24/djredcledockerjenkins:latest &&
                          docker-compose -f /opt/myapp/docker-compose.yml up -d --force-recreate
                        "
                    '''
                }
            }
        }

    }


}
