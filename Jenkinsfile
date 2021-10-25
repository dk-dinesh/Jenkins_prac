pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
        cron('0 0 * * *')
    }
        stages {
            stage("Compile") {
                steps {
                    echo "Compilation done"
                    }
                }
            stage("Unit test") {
            steps {
                sh "python python_program_test.py"
                }
            }
        }
    }