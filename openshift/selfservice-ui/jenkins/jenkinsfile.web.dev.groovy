#!/usr/bin/env groovy
import java.util.Date
import java.text.SimpleDateFormat
import groovy.json.*

// Load Common Variables and utils
common = ""
node{
  common = load "../workspace@script/openshift/selfservice-ui/jenkins/jenkinsfile.common.groovy"
}

// You shouldn't have to edit these if you're following the conventions
WEB_BUILD = WEB_NAME + "-build"
IMAGESTREAM_NAME = WEB_NAME
NAMESPACE = 'oultzp'
TOOLS_TAG = 'tools'
NAMESPACE_BUILD = "${NAMESPACE}"  + '-' + "${TOOLS_TAG}"
ROCKETCHAT_CHANNEL='#bcsc-ss-bot'


stage('Build ' + WEB_NAME) {
  node{
    openshift.withProject() {
      try{
        // Make sure the frontend build configs exist
        common.ensureBuildExists(WEB_BUILD,"openshift/selfservice-ui/web-build.yaml")

        // Build and verify the app
        common.buildAndVerify(WEB_BUILD)

        ROCKETCHAT_TOKEN = sh (
                    script: """oc get secret/rocketchat-token-secret -n ${NAMESPACE_BUILD} -o template --template="{{.data.ROCKETCHAT_TOKEN}}" | base64 --decode""",
                        returnStdout: true).trim()

        COMMENTS = '{"username":"bcsc-jedi","icon_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTizwY92yvdrPaFVBlbw6JW9fiDxZrogj10UvkKGnp66xLNx3io5Q&s","text":"SelfService-UI build Success 🚀","attachments":[{"title":"Selfservice-ui build","title_link":${BUILD_URL},"text":"Selfservice-ui build details:","image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwc_SWm-J_9OPSJVzUqxibPHZI55EBwpOB-JPeY0drU64YENdUWA&s","color":"#1ee321"}]}'

        common.rocketChatNotificaiton("${ROCKETCHAT_TOKEN}", "${ROCKETCHAT_CHANNEL}", "${COMMENT}" )
        // Don't tag with BUILD_ID so the pruner can do it's job; it won't delete tagged images.
        // Tag the images for deployment based on the image's hash
        IMAGE_HASH = common.getLatestHash(IMAGESTREAM_NAME)          
        echo ">> IMAGE_HASH: ${IMAGE_HASH}"

      }catch(error){
        FAILED_COMMENT = '{"username":"bcsc-jedi","icon_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTizwY92yvdrPaFVBlbw6JW9fiDxZrogj10UvkKGnp66xLNx3io5Q&s","text":"SelfService-UI build Failure 🤕","attachments":[{"title":"Selfservice-ui build","title_link":${BUILD_URL},"text":"Selfservice-ui build details:","image_url":"https://i.imgflip.com/1czxka.jpg","color":"#e3211e"}]}'

        common.rocketChatNotificaiton("${ROCKETCHAT_TOKEN}", "${ROCKETCHAT_CHANNEL}", "${FAILED_COMMENT}" )
        // common.notifyError(
        //   "${WEB_BUILD} Build Broken 🤕",
        //   "Author:${env.CHANGE_AUTHOR_DISPLAY_NAME}\r\nError:'${error.message}'"
        // )
        throw error
      }
    }
  }
}
  
  // We have Functional tests in our API project, commenting out these stages
  // as we do not currently have e2e tests within our frontend.
  // // Creating Emphemeral post-gress instance for testing
  // stage('Emphemeral Test Environment'){
  //   node{
  //     try{
  //       echo "Creating Ephemeral Postgress instance for testing"
  //       POSTGRESS = sh (
  //         script: """oc project jag-shuber-tools; oc process -f "${work_space}/openshift/test/frontend-deploy.json" | oc create -f -; oc process -f "${work_space}/openshift/test/api-postgress-ephemeral.json" | oc create -f - """)
  //         echo ">> POSTGRESS: ${POSTGRESS}" 
        
  //     } catch(error){
  //       echo "Error in creating postgress instance"
  //       throw error
  //     }
  //   }
  // }

  // //Running functional Test cases - in tools project
  // stage('Run Test Cases'){
  //   node{
  //   try{
  //     echo "Run Test Case scripts here"
  //     POSTGRESS_DEL = sh (
  //       script: """oc project jag-shuber-tools; oc process -f "${work_space}/openshift/test/frontend-deploy.json" | oc delete -f -; oc process -f "${work_space}/openshift/test/api-postgress-ephemeral.json" | oc delete -f - """)
  //       echo ">> ${POSTGRESS_DEL}"
  //     echo "postgress instance deleted successfully"
  //   } catch(error){
  //     echo "Error while test cases are running"
  //     throw error
  //     }
  //   }
  // }

// Deploying to Dev
stage("Deploy to ${common.web_environments.dev.name}") {
  def environment = common.web_environments.dev.tag
  def url = common.web_environments.dev.url
  node{
    try{
      common.deployAndVerify(IMAGE_HASH,environment,IMAGESTREAM_NAME)
      ROCKETCHAT_TOKEN = sh (
                    script: """oc get secret/rocketchat-token-secret -n ${NAMESPACE_BUILD} -o template --template="{{.data.ROCKETCHAT_TOKEN}}" | base64 --decode""",
                        returnStdout: true).trim()

      COMMENT = '{"username":"bcsc-jedi","icon_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTizwY92yvdrPaFVBlbw6JW9fiDxZrogj10UvkKGnp66xLNx3io5Q&s","text":"SelfService-UI Deployment Success 🚀","attachments":[{"title":"Selfservice-ui Deployment","title_link":${BUILD_URL},"text":"Selfservice-ui build details:","image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwc_SWm-J_9OPSJVzUqxibPHZI55EBwpOB-JPeY0drU64YENdUWA&s","color":"#1ee321"}]}'

      common.rocketChatNotificaiton("${ROCKETCHAT_TOKEN}", "${ROCKETCHAT_CHANNEL}", "${COMMENT}" )
    //   common.notifyNewDeployment(environment,url,"Deploy to ${common.environments.test.name}?")
    }catch(error){
      // common.notifyDeploymentError(environment,error)
      FAILED_COMMENT = '{"username":"bcsc-jedi","icon_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTizwY92yvdrPaFVBlbw6JW9fiDxZrogj10UvkKGnp66xLNx3io5Q&s","text":"SelfService-UI Deployment Failure 🤕","attachments":[{"title":"Selfservice-ui Deployment","title_link":${BUILD_URL},"text":"Selfservice-ui build details:","image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWWlY9blSXitK3hnPaxoUlZPiV3oJRcGrq3STQDwKsExo4bmgP&s","color":"#e3211e"}]}'

      common.rocketChatNotificaiton("${ROCKETCHAT_TOKEN}", "${ROCKETCHAT_CHANNEL}", "${FAILED_COMMENT}" )
      throw error
    }
  }
}


// // Deploying to Test
// stage("Deploy to ${common.environments.test.name}") {
//   def environment = common.environments.test.tag
//   def url = common.environments.test.url
//   timeout(time:7, unit: 'DAYS'){ input "Deploy to ${environment}?"}
//   node{
//     try{
//       common.deployAndVerify(IMAGE_HASH,environment,IMAGESTREAM_NAME)
//       common.notifyNewDeployment(environment,url,"Tag for ${common.environments.prod.name}?")
//     }catch(error){
//       common.notifyDeploymentError(environment,error)
//       throw error
//     }
//   }
// }

// // Tag for Prod
// stage("Tag for ${common.environments.prod.name}") {
//   def environment = common.environments.prod.tag
//   timeout(time:7, unit: 'DAYS'){ input "Tag for ${common.environments.prod.name}?"}
//   node{
//     try{
//       common.tagImage(IMAGE_HASH,environment,IMAGESTREAM_NAME)
//       common.notifyGood(
//         "${common.APP_NAME} tagged for ${common.environments.prod.name}",
//         "Start production pipeline to push new images"
//       )
//     }catch(error){
//       common.notifyError(
//         "Couldn't tag ${common.APP_NAME} for ${common.environments.prod.name} 🤕",
//         "Error: '${error.message}'"
//       )
//       throw error
//     }
//   }
// }