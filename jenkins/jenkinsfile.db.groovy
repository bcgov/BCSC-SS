// Common component parameters
NAMESPACE = 'oultzp'
TOOLS_TAG = 'tools'
NAMESPACE_BUILD = "${NAMESPACE}"  + '-' + "${TOOLS_TAG}"
ROCKETCHAT_CHANNEL='#bcsc-ss-bot'
BUILD_PHASE = "build"
DEPLOYMENT_PHASE = "Deployment"
// Load Common Variables and utils
common = ""
node{
  common = load "../workspace@script/jenkins/jenkinsfile.common.groovy"
  ROCKETCHAT_TOKEN = sh (
                    script: """oc get secret/rocketchat-token-secret -n ${NAMESPACE_BUILD} -o template --template="{{.data.ROCKETCHAT_TOKEN}}" | base64 --decode""",
                        returnStdout: true).trim()
}


// Selfservice-db parameters
DB_BUILD = common.DB_NAME + "-build"
DB_IMAGESTREAM_NAME = common.DB_NAME

// Database Build
stage('Build ' + DB_IMAGESTREAM_NAME) {
  node{
    openshift.withProject() {
      try{
        // Make sure the frontend build configs exist
        common.ensureBuildExists(DB_BUILD,"openshift/selfservice-db/db-build.yaml")
        // Build and verify the app
        common.buildAndVerify(DB_BUILD)
        
        // Tag the images for deployment based on the image's hash
        DB_IMAGE_HASH = common.getLatestHash(DB_IMAGESTREAM_NAME)          
        echo ">> DB_IMAGE_HASH: ${DB_IMAGE_HASH}"

        //Success DB-Build Notification
        common.successNotificaiton(ROCKETCHAT_TOKEN, DB_IMAGESTREAM_NAME, BUILD_PHASE )
      }catch(error){
        // failure DB Build Notification
        common.failureNotificaiton(ROCKETCHAT_TOKEN, DB_IMAGESTREAM_NAME, BUILD_PHASE )
        throw error
      }
    }
  }
}

