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

// Selfservice-UI Parameters
WEB_BUILD = common.WEB_NAME + "-build"
WEB_IMAGESTREAM_NAME = common.WEB_NAME

// Selfservice-db parameters
DB_BUILD = common.DB_NAME + "-build"
DB_IMAGESTREAM_NAME = common.DB_NAME

// SelfService-Api parameters
API_BUILD = common.API_NAME + "-build"
API_IMAGESTREAM_NAME = common.API_NAME


stage('Build ' + WEB_IMAGESTREAM_NAME) {
  node{
    openshift.withProject() {
    try{
        // Make sure the frontend build configs exist
        common.ensureBuildExists(WEB_BUILD,"openshift/selfservice-ui/web-build.yaml")
        // Build and verify the app
        common.buildAndVerify(WEB_BUILD)
        
        // Don't tag with BUILD_ID so the pruner can do it's job; it won't delete tagged images.
        // Tag the images for deployment based on the image's hash
        WEB_IMAGE_HASH = common.getLatestHash(WEB_IMAGESTREAM_NAME)          
        echo ">> WEB_IMAGE_HASH: ${WEB_IMAGE_HASH}"
        
        // Success UI-Build Notification
        common.successNotificaiton(ROCKETCHAT_TOKEN, WEB_IMAGESTREAM_NAME, BUILD_PHASE )

    }catch(error){
        //Failure UI Build Notification
        common.failureNotificaiton(ROCKETCHAT_TOKEN, WEB_IMAGESTREAM_NAME, BUILD_PHASE )
        throw error
    }
    }
  }
}

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

stage('Build ' + API_IMAGESTREAM_NAME) {
  node{
    openshift.withProject() {
      try{
        // Make sure the frontend build configs exist
        common.ensureBuildExists(API_BUILD,"openshift/selfservice-api/api-build.yaml")
        // Build and verify the app
        common.buildAndVerify(API_BUILD)

        // Tag the images for deployment based on the image's hash
        API_IMAGE_HASH = common.getLatestHash(API_IMAGESTREAM_NAME)          
        echo ">> API_IMAGE_HASH: ${API_IMAGE_HASH}"

        //Success DB-Build Notification
        common.successNotificaiton(ROCKETCHAT_TOKEN, API_IMAGESTREAM_NAME, BUILD_PHASE)
      }catch(error){
        // failure DB Build Notification
        common.failureNotificaiton(ROCKETCHAT_TOKEN, API_IMAGESTREAM_NAME, BUILD_PHASE )
        throw error
      }
    }
  }
}

// Deploying WEB to test
stage("Deploy" + WEB_IMAGESTREAM_NAME + "to ${common.web_environments.test.name}") {
  def environment = common.web_environments.test.tag
  def url = common.web_environments.test.url
  node{
    try{
      common.deployAndVerify(WEB_IMAGE_HASH,environment,WEB_IMAGESTREAM_NAME)

      // WEB Deployment Success notification
      common.successNotificaiton(ROCKETCHAT_TOKEN, WEB_IMAGESTREAM_NAME, DEPLOYMENT_PHASE )
    }catch(error){
      // Web Deployment Failure Notification
      common.failureNotificaiton(ROCKETCHAT_TOKEN, WEB_IMAGESTREAM_NAME, DEPLOYMENT_PHASE )
      throw error
    }
  }
}

// Deploying DB to test
stage("Deploy to" + DB_NAME + "${common.db_environments.test.name}") {
  def environment = common.db_environments.test.tag
  def url = common.db_environments.test.url
  node{
    try{
      common.deployAndVerify(DB_IMAGE_HASH,environment,DB_IMAGESTREAM_NAME)

      // DB Deployment Success notification
      common.successNotificaiton(ROCKETCHAT_TOKEN, DB_IMAGESTREAM_NAME, DEPLOYMENT_PHASE )
    }catch(error){
      // DB Deployment Failure notification
      common.failureNotificaiton(ROCKETCHAT_TOKEN, DB_IMAGESTREAM_NAME, DEPLOYMENT_PHASE )
      throw error
    }
}
}

// Deploying API to test
stage("Deploy to" + API_NAME + "${common.api_environments.test.name}") {
  def environment = common.api_environments.test.tag
  def url = common.api_environments.test.url
  node{
    try{
      common.deployAndVerify(API_IMAGE_HASH,environment,API_IMAGESTREAM_NAME)

      // DB Deployment Success notification
      common.successNotificaiton(ROCKETCHAT_TOKEN, API_IMAGESTREAM_NAME, DEPLOYMENT_PHASE )
    }catch(error){
      // DB Deployment Failure notification
      common.failureNotificaiton(ROCKETCHAT_TOKEN, API_IMAGESTREAM_NAME, DEPLOYMENT_PHASE )
      throw error
    }
  }
}  