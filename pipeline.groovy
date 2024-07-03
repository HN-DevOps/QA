pipeline {
    agent { label 'Staging Node Runner' }

    environment {
        VIRTUAL_ENV = 'env'
        GIT_URL = 'https://github.com/NajlaGIT/SB-twin.git'
        BRANCH = 'main'
    }

    stages {
        stage('Get code from Git') {
            steps {
                git branch: "${BRANCH}", url: "${GIT_URL}"
            }
        }

        stage('Setup Environment') {
            steps {
                script {
                    try {
                        sh """
                            #!/bin/bash
                            python3 -m venv ${VIRTUAL_ENV}
                            . ${VIRTUAL_ENV}/bin/activate
                        """
                    } catch (Exception e) {
                        echo "Failed to create virtual environment: ${e.message}"
                        error("Failed to create virtual environment")
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    try {
                        sh """
                            #!/bin/bash
                            . ${VIRTUAL_ENV}/bin/activate
                            python3 -m pip install --upgrade pip
                            python3 -m pip install -r requirements.txt
                        """
                    } catch (Exception e) {
                        echo "Failed to install dependencies: ${e.message}"
                        error("Failed to install dependencies")
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    try {
                        sh """
                            #!/bin/bash
                            . ${VIRTUAL_ENV}/bin/activate
                            pytest
                        """
                    } catch (Exception e) {
                        echo "Failed to run tests: ${e.message}"
                        error("Failed to run tests")
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'One or more tests failed.'
        }
    }
}
