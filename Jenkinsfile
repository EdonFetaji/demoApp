node {
    def frontend, backend
    def imageTag = "${env.BRANCH_NAME}-${env.BUILD_NUMBER}"
    def latestTag = "${env.BRANCH_NAME}-latest"

    stage('Clean Workspace') {
        deleteDir()
    }

    stage('Clone Repository') {
        checkout([
            $class: 'GitSCM',
            branches: [[name: '*/main']],
            extensions: [[
                $class: 'CleanBeforeCheckout'
            ]],
            userRemoteConfigs: [[
                url: 'https://github.com/EdonFetaji/demoApp.git',
                credentialsId: 'github-credentials'
            ]]
        ])
        
        // Debugging
        sh 'pwd'
        sh 'ls -la'
    }

    stage('Build Images') {
        frontend = docker.build("edon505/demo-frontend", "./frontend")
        backend  = docker.build("edon505/demo-backend", "./backend")
    }

    stage('Push Images') {
        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
            frontend.push(imageTag)
            frontend.push(latestTag)
            backend.push(imageTag)
            backend.push(latestTag)
        }
        echo "Docker images pushed for branch: ${env.BRANCH_NAME}"
    }
}
