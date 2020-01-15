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
  echo "Deploying ${DB_NAME} to ${destination}"
  tagImage(srcHash, destination, imageStream)
  // verify deployment
  openshiftVerifyDeployment(
    deploymentConfig: DB_NAME, 
    namespace: "${PROJECT_PREFIX}-${destination}", 
    waitTime: '9000000'
  )
}

@NonCPS
String getUrlForRoute(String routeName, String projectNameSpace = '') {

  def nameSpaceFlag = ''
  if(projectNameSpace?.trim()) {
    nameSpaceFlag = "-n ${projectNameSpace}"
  }
  def url = sh (
    script: """ 'https://' + `oc get routes jenkins -o json | jq '.spec.host' | xargs echo` + '/' | echo $url""",
    returnStdout: true
  ).trim()

  return url
}

@NonCPS
def rocketChatNotificaiton(token, channel, comments) {
  // def payload = JsonOutput.toJson([text: comments, channel: channel])
  def rocketChatUrl = "https://chat.pathfinder.gov.bc.ca/hooks/" + "${token}"

  sh(returnStdout: true,
     script: "curl -X POST -H 'Content-Type: application/json' --data ${comments} ${rocketChatUrl}")
}

// def notifyGood(title,description,buttons=[]){
//   if(env.SLACK_HOOK){
//     slackNotify(
//       title,
//       description,
//       'good',
//       env.SLACK_HOOK,
//       SLACK_MAIN_CHANNEL,
//       buttons
//     )
//   }else{
//     echo "Would notify goodness via slack";
//   }
// }

// def notifyNewDeployment(environment,url,nextButtonText){
//     notifyGood(
//       "New ${APP_NAME} in ${environment} 🚀",
//       "Changes: ${getChangeString()}",
//       [
//         [
//           type: "button",
//           text: "View New Version",           
//           url: "${url}"
//         ],
//         [
//           type: "button",            
//           text: nextButtonText,
//           style: "primary",              
//           url: "${currentBuild.absoluteUrl}/input"
//         ]
//       ]
//     )
// }

// def notifyError(title,description){
//   if(env.SLACK_HOOK){
//     slackNotify(
//       title,
//       description,
//       'danger',
//       env.SLACK_HOOK,
//       SLACK_DEV_CHANNEL,
//       [
//         [
//           type: "button",
//           text: "View Build Logs",
//           style:"danger",        
//           url: "${currentBuild.absoluteUrl}/console"
//         ]
//       ]
//     )
//   }else{
//     echo "Would notify error via slack";
//   }
// }

// def notifyDeploymentError(environment,error){
//   notifyError(
//     "Couldn't deploy ${APP_NAME} to ${environment} 🤕",
//     "The latest deployment of the ${APP_NAME} to ${environment} seems to have failed\n'${error.message}'"
//   )
// }

return this