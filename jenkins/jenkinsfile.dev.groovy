// Common component parameters
NAMESPACE = 'oultzp'
TOOLS_TAG = 'tools'
NAMESPACE_BUILD = "${NAMESPACE}"  + '-' + "${TOOLS_TAG}"
ROCKETCHAT_CHANNEL='#bcsc-ss-bot'
BUILD_PHASE = "build"
TEST_PHASE = "Test"
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
        common.ensureBuildExists(WEB_BUILD,"openshift/selfservice-ui/web-build_test.yaml")
        // Build and verify the app
        common.buildAndVerify(WEB_BUILD)
        
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

stage('Build ' + API_IMAGESTREAM_NAME) {
  node{
    openshift.withProject() {
      try{
        // Make sure the frontend build configs exist
        common.ensureBuildExists(API_IMAGESTREAM_NAME,"openshift/selfservice-api/api-build.yaml")
        // Build and verify the app
        common.buildAndVerify(API_BUILD)

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

// Integration testing for API
stage('Integration Test run for API ' + API_IMAGESTREAM_NAME) {
  def db_environment = common.db_environments.tools.tag
  def api_environment = common.db_environments.tools.tag
  db_tag = "prod"
  def api_tag = common.api_environments.dev.tag
  node{
    openshift.withProject() {
      try{
        // Make sure the frontend build configs exist
        common.createTestDeployment(DB_IMAGESTREAM_NAME,"openshift/selfservice-db/db-deploy.yaml")
        // Tag the images for deployment based on the image's hash
        DB_IMAGE_HASH = common.getLatestHash(DB_IMAGESTREAM_NAME, db_tag)          
        echo ">> DB_IMAGE_HASH: ${DB_IMAGE_HASH}"
        // Verify deloyment
        common.deployAndVerify(DB_IMAGE_HASH,db_environment,DB_IMAGESTREAM_NAME)

        // Make sure the frontend build configs exist
        common.createTestDeployment(API_IMAGESTREAM_NAME,"openshift/selfservice-api/api-deploy-test.yaml")
        // Tag the images for deployment based on the image's hash
        API_IMAGE_HASH = common.getLatestHash(API_IMAGESTREAM_NAME, api_tag)          
        echo ">> API_IMAGE_HASH: ${API_IMAGE_HASH}"
        // Verify deloyment
        common.deployAndVerify(API_IMAGE_HASH,api_environment,API_IMAGESTREAM_NAME)
        //Success DB-Build Notification
        common.testSuccessNotificaiton(ROCKETCHAT_TOKEN, API_IMAGESTREAM_NAME, TEST_PHASE)
      }catch(error){
        // failure DB Build Notification
        common.failureNotificaiton(ROCKETCHAT_TOKEN, API_IMAGESTREAM_NAME, TEST_PHASE )
        throw error
      }
    }
  }
}

// Deploying WEB to Dev
stage("Deploy" + WEB_IMAGESTREAM_NAME + "to ${common.web_environments.dev.name}") {
  def environment = common.web_environments.dev.tag
  def url = common.web_environments.dev.url
  node{
    try{
      // Tag the images for deployment based on the image's hash
      WEB_IMAGE_HASH = common.getLatestHash(WEB_IMAGESTREAM_NAME, environment)          
      echo ">> WEB_IMAGE_HASH: ${WEB_IMAGE_HASH}"

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

// Deploying DB to Dev
stage("Deploy to" + DB_NAME + "${common.db_environments.dev.name}") {
  def environment = common.db_environments.dev.tag
  db_tag = "prod"
  def url = common.db_environments.dev.url
  node{
    try{
      // Tag the images for deployment based on the image's hash
      DB_IMAGE_HASH = common.getLatestHash(DB_IMAGESTREAM_NAME, db_tag)          
      echo ">> DB_IMAGE_HASH: ${DB_IMAGE_HASH}"

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

// Deploying API to Dev
stage("Deploy to" + API_NAME + "${common.api_environments.dev.name}") {
  def environment = common.api_environments.dev.tag
  def url = common.api_environments.dev.url
  node{
    try{
      // Tag the images for deployment based on the image's hash
      API_IMAGE_HASH = common.getLatestHash(API_IMAGESTREAM_NAME, environment)          
      echo ">> API_IMAGE_HASH: ${API_IMAGE_HASH}"

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