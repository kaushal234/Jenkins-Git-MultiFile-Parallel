pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    echo "Installing Dependencies..."
                    python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Parallel Tasks') {

            parallel {

                stage('Run Application') {
                    steps {
                        sh '''
                            python3 app.py
                        '''
                    }
                }

                stage('Run Tests') {
                    steps {
                        sh '''
                            python3 test_app.py
                        '''
                    }
                }

                stage('Run Lint') {
                    steps {
                        sh '''
                            python3 lint.py
                        '''
                    }
                }

            }
        }

        stage('Summary') {
            steps {
                echo "All Parallel Tasks Completed Successfully!"
            }
        }
    }

    post {

        success {
            echo "Pipeline completed successfully."
        }

        failure {
            echo "Pipeline failed."
        }

        always {
            echo "Build Finished."
        }

    }
}
