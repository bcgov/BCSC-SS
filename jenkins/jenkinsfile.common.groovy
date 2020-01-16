#!/usr/bin/env groovy
import java.util.Date
import java.text.SimpleDateFormat
import groovy.json.*

// Load shared devops utils
library identifier: 'devops-library@master', retriever: modernSCM([
  $class: 'GitSCMSource',
  remote: 'https://github.com/BCDevOps/jenkins-pipeline-shared-lib.git'
])

// Edit your app's name below
WEB_NAME = 'selfservice-ui'
API_NAME = 'selfservice-api'
DB_NAME =  'selfservice-db'

// You shouldn't have to edit these if you're following the conventions
ROCKETCHAT_CHANNEL='#bcsc-ss-bot'
PATHFINDER_URL = "pathfinder.gov.bc.ca"
PROJECT_PREFIX = 'oultzp'


class AppEnvironment{
  String name
  String tag
  String url
}


web_environments = [
  dev:new AppEnvironment(name:'Development',tag:'dev',url:"https://${WEB_NAME}-${PROJECT_PREFIX}-dev.${PATHFINDER_URL}/"),
  test:new AppEnvironment(name:'Test',tag:'test',url:"https://${WEB_NAME}-${PROJECT_PREFIX}-test.${PATHFINDER_URL}/"),
  prod:new AppEnvironment(name:'Prod',tag:'prod',url:"https://${WEB_NAME}-${PROJECT_PREFIX}-prod.${PATHFINDER_URL}/")
]

api_environments = [
  dev:new AppEnvironment(name:'Development',tag:'dev',url:"https://${API_NAME}-${PROJECT_PREFIX}-dev.${PATHFINDER_URL}/"),
  test:new AppEnvironment(name:'Test',tag:'test',url:"https://${API_NAME}-${PROJECT_PREFIX}-test.${PATHFINDER_URL}/"),
  prod:new AppEnvironment(name:'Prod',tag:'prod',url:"https://${API_NAME}-${PROJECT_PREFIX}-prod.${PATHFINDER_URL}/")
]

db_environments = [
  dev:new AppEnvironment(name:'Development',tag:'dev',url:"https://${DB_NAME}-${PROJECT_PREFIX}-dev.${PATHFINDER_URL}/"),
  test:new AppEnvironment(name:'Test',tag:'test',url:"https://${DB_NAME}-${PROJECT_PREFIX}-test.${PATHFINDER_URL}/"),
  prod:new AppEnvironment(name:'Prod',tag:'prod',url:"https://${DB_NAME}-${PROJECT_PREFIX}-prod.${PATHFINDER_URL}/")
]

// Gets the container hash for the latest image in an image stream
def getLatestHash(imageStreamName){
  return sh (
    script: """oc get istag ${imageStreamName}:dev -o=jsonpath='{@.image.metadata.name}' | sed -e 's/sha256://g'""",
    returnStdout: true
  ).trim()
}

def ensureBuildExists(buildConfigName,templatePath){
  if(!openshift.selector( "bc/${buildConfigName}")){
    newBuildConfig = sh ( """oc process -f "${env.WORKSPACE}/../workspace@script/${templatePath}" | oc create -f - """)
    echo ">> ${newBuildConfig}"
  }else{
    echo "Build Config '${buildConfigName}' already exists"
  }
}

def triggerBuild(buildConfigName){
  echo "Building: ${buildConfigName}"
  openshiftBuild bldCfg: buildConfigName, showBuildLogs: 'true', waitTime: '9000000'  
}

def verifyBuild(buildConfigName){
  openshiftVerifyBuild bldCfg: buildConfigName, showBuildLogs: 'true', waitTime: '9000000'
}

def buildAndVerify(buildConfigName){
  echo "Building: ${buildConfigName}"
  openshiftBuild bldCfg: buildConfigName, showBuildLogs: 'true', waitTime: '9000000'
  openshiftVerifyBuild bldCfg: buildConfigName, showBuildLogs: 'true', waitTime: '9000000'
}

def tagImage(srcHash, destination, imageStream){
  openshiftTag(
    destStream: imageStream, 
    verbose: 'true', 
    destTag: destination, 
    srcStream: imageStream, 
    srcTag: srcHash, 
    waitTime: '9000000'
  )
}

def deployAndVerify(srcHash, destination, imageStream){
  echo "Deploying ${imageStream} to ${destination}"
  tagImage(srcHash, destination, imageStream)
  // verify deployment
  openshiftVerifyDeployment(
    deploymentConfig: "${imageStream}", 
    namespace: "${PROJECT_PREFIX}-${destination}", 
    waitTime: '900000'
  )
}

// @NonCPS
// String getUrlForRoute(String routeName, String projectNameSpace = '') {

//   def nameSpaceFlag = ''
//   if(projectNameSpace?.trim()) {
//     nameSpaceFlag = "-n ${projectNameSpace}"
//   }
//   def url = sh (
//     script: """ 'https://' + `oc get routes jenkins -o json | jq '.spec.host' | xargs echo` + '/' | echo $url""",
//     returnStdout: true
//   ).trim()

//   return url
// }

def rocketchat_token(){
    return sh (
        script: """oc get secret/rocketchat-token-secret -n ${NAMESPACE_BUILD} -o template --template="{{.data.ROCKETCHAT_TOKEN}}" | base64 --decode""",
        returnStdout: true
  ).trim()
}

@NonCPS
def rocketChatNotificaiton(app_name) {
  def token = rocketchat_token()
  def rocketChatUrl = "https://chat.pathfinder.gov.bc.ca/hooks/" + "${token}"
  build_url = "${currentBuild.absoluteUrl}console"
  attachment = ["title":"${app_name} Deployment","title_link":"${build_url}", "image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwc_SWm-J_9OPSJVzUqxibPHZI55EBwpOB-JPeY0drU64YENdUWA&s","color":"#1ee321"]

  def payload = JsonOutput.toJson([username: "bcsc-jedi", icon_url: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTizwY92yvdrPaFVBlbw6JW9fiDxZrogj10UvkKGnp66xLNx3io5Q&s", text: "${app_name} Deployment Success 🚀", attachments: [attachment], channel: "${ROCKETCHAT_CHANNEL}"])
  sh(returnStdout: true,
     script: "curl -X POST -H 'Content-Type: application/json' --data \'${payload}\' ${rocketChatUrl}")
}


return this