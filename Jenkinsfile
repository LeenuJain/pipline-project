pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Code Quality') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pip install flake8
                    flake8 src\\ tests\\ --count --select=E9,F63,F7,F82 --show-source --statistics
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pytest test\\ --junitxml=test-reports/results.xml --cov=src --cov-report=xml:coverage-reports/coverage.xml
                '''
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                    recordCoverage(tools: [[parser: 'COBERTURA', pattern: 'coverage-reports/coverage.xml']])
                }
            }
        }
        
        stage('Build Package') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pip install wheel
                    python setup.py bdist_wheel
                '''
            }
            post {
                success {
                    archiveArtifacts artifacts: 'dist/*.whl', fingerprint: true
                }
            }
        }
    }
}
