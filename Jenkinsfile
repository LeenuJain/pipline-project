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
                script {
                    if (isUnix()) {
                        sh '''
                            python -m venv venv
                            . venv/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            python -m venv venv
                            venv\\Scripts\\activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }
        
        stage('Code Quality') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            . venv/bin/activate
                            pip install flake8
                            flake8 src/ tests/ --count --select=E9,F63,F7,F82 --show-source --statistics
                        '''
                    } else {
                        bat '''
                            venv\\Scripts\\activate
                            pip install flake8
                            flake8 src\\ tests\\ --count --select=E9,F63,F7,F82 --show-source --statistics
                        '''
                    }
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            . venv/bin/activate
                            pytest tests/ --junitxml=test-reports/results.xml --cov=src --cov-report=xml:coverage-reports/coverage.xml
                        '''
                    } else {
                        bat '''
                            venv\\Scripts\\activate
                            pytest tests\\ --junitxml=test-reports/results.xml --cov=src --cov-report=xml:coverage-reports/coverage.xml
                        '''
                    }
                }
            }
            post {
                always {
                    junit 'results.xml'
                    recordCoverage(tools: [[parser: 'COBERTURA', pattern: 'coverage-reports/coverage.xml']])
                }
            }
        }
        
        stage('Build Package') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            . venv/bin/activate
                            pip install wheel
                            python setup.py bdist_wheel
                        '''
                    } else {
                        bat '''
                            venv\\Scripts\\activate
                            pip install wheel
                            python setup.py bdist_wheel
                        '''
                    }
                }
            }
            post {
                success {
                    archiveArtifacts artifacts: 'dist/*.whl', fingerprint: true
                }
            }
        }
    }
}
