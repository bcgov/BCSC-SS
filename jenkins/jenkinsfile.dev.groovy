
// Load Common Variables and utils
common = ""
node{
  common = load "../workspace@script/jenkins/jenkinsfile.common.groovy"
}

// Common component parameters
NAMESPACE = 'oultzp'
TOOLS_TAG = 'tools'
NAMESPACE_BUILD = "${NAMESPACE}"  + '-' + "${TOOLS_TAG}"
ROCKETCHAT_CHANNEL='#bcsc-ss-bot'


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
        // common.buildAndVerify(WEB_BUILD)
        
        // // Don't tag with BUILD_ID so the pruner can do it's job; it won't delete tagged images.
        // // Tag the images for deployment based on the image's hash
        // WEB_IMAGE_HASH = common.getLatestHash(WEB_IMAGESTREAM_NAME)          
        // echo ">> WEB_IMAGE_HASH: ${WEB_IMAGE_HASH}"

        // Success UI-Build Notification
        
        // ROCKETCHAT_TOKEN = sh (
        //             script: """oc get secret/rocketchat-token-secret -n ${NAMESPACE_BUILD} -o template --template="{{.data.ROCKETCHAT_TOKEN}}" | base64 --decode""",
        //                 returnStdout: true).trim()
        common.rocketChatNotificaiton(WEB_IMAGESTREAM_NAME )

    }catch(error){
        //Failure UI Build Notification
        // FAILED_COMMENT = '{"username":"bcsc-jedi","icon_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTizwY92yvdrPaFVBlbw6JW9fiDxZrogj10UvkKGnp66xLNx3io5Q&s","text":"SelfService-UI build Failure 🤕","attachments":[{"title":"Selfservice-ui build","title_link":${BUILD_URL},"text":"Selfservice-ui build details:","image_url":"https://i.imgflip.com/1czxka.jpg","color":"#e3211e"}]}'

        // common.rocketChatNotificaiton("${ROCKETCHAT_TOKEN}", "${ROCKETCHAT_CHANNEL}", "${FAILED_COMMENT}" )
        throw error
    }
    }
  }
}

// stage('Build ' + DB_IMAGESTREAM_NAME) {
//   node{
//     openshift.withProject() {
//       try{
//         // Make sure the frontend build configs exist
//         common.ensureBuildExists(DB_BUILD,"openshift/selfservice-db/db-build.yaml")
//         // Build and verify the app
//         common.buildAndVerify(DB_BUILD)

//         //Success DB-Build Notification
//         COMMENT = '{"username":"bcsc-jedi","icon_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTizwY92yvdrPaFVBlbw6JW9fiDxZrogj10UvkKGnp66xLNx3io5Q&s","text":"SelfService-DB build Success 🚀","attachments":[{"title":"Selfservice-DB build","title_link":${BUILD_URL},"text":"Selfservice-db build details:","image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwc_SWm-J_9OPSJVzUqxibPHZI55EBwpOB-JPeY0drU64YENdUWA&s","color":"#1ee321"}]}'
//         ROCKETCHAT_TOKEN = sh (
//                     script: """oc get secret/rocketchat-token-secret -n ${NAMESPACE_BUILD} -o template --template="{{.data.ROCKETCHAT_TOKEN}}" | base64 --decode""",
//                         returnStdout: true).trim()
//         common.rocketChatNotificaiton("${ROCKETCHAT_TOKEN}", "${ROCKETCHAT_CHANNEL}", "${COMMENT}" )
        
//         // Tag the images for deployment based on the image's hash
//         DB_IMAGE_HASH = common.getLatestHash(DB_IMAGESTREAM_NAME)          
//         echo ">> DB_IMAGE_HASH: ${DB_IMAGE_HASH}"

//       }catch(error){
//         // failure DB Build Notification
//         FAILED_COMMENT = '{"username":"bcsc-jedi","icon_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTizwY92yvdrPaFVBlbw6JW9fiDxZrogj10UvkKGnp66xLNx3io5Q&s","text":"SelfService-DB build Failure 🤕","attachments":[{"title":"Selfservice-DB build","title_link":${BUILD_URL},"text":"Selfservice-DB build details:","image_url":"https://i.imgflip.com/1czxka.jpg","color":"#e3211e"}]}'
//         common.rocketChatNotificaiton("${ROCKETCHAT_TOKEN}", "${ROCKETCHAT_CHANNEL}", "${FAILED_COMMENT}" )
//         throw error
//       }
//     }
//   }
// }

// stage('Build ' + API_IMAGESTREAM_NAME) {
//   node{
//     openshift.withProject() {
//       try{
//         // Make sure the frontend build configs exist
//         common.ensureBuildExists(API_BUILD,"openshift/selfservice-api/api-build.yaml")
//         // Build and verify the app
//         common.buildAndVerify(API_BUILD)

//         //Success DB-Build Notification
//         COMMENT = '{"username":"bcsc-jedi","icon_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTizwY92yvdrPaFVBlbw6JW9fiDxZrogj10UvkKGnp66xLNx3io5Q&s","text":"SelfService-API build Success 🚀","attachments":[{"title":"Selfservice-API build","title_link":${BUILD_URL},"text":"Selfservice-API build details:","image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwc_SWm-J_9OPSJVzUqxibPHZI55EBwpOB-JPeY0drU64YENdUWA&s","color":"#1ee321"}]}'
//         ROCKETCHAT_TOKEN = sh (
//                     script: """oc get secret/rocketchat-token-secret -n ${NAMESPACE_BUILD} -o template --template="{{.data.ROCKETCHAT_TOKEN}}" | base64 --decode""",
//                         returnStdout: true).trim()
//         common.rocketChatNotificaiton("${ROCKETCHAT_TOKEN}", "${ROCKETCHAT_CHANNEL}", "${COMMENT}" )
        
//         // Tag the images for deployment based on the image's hash
//         API_IMAGE_HASH = common.getLatestHash(API_IMAGESTREAM_NAME)          
//         echo ">> API_IMAGE_HASH: ${API_IMAGE_HASH}"

//       }catch(error){
//         // failure DB Build Notification
//         FAILED_COMMENT = '{"username":"bcsc-jedi","icon_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTizwY92yvdrPaFVBlbw6JW9fiDxZrogj10UvkKGnp66xLNx3io5Q&s","text":"SelfService-DB build Failure 🤕","attachments":[{"title":"Selfservice-API build","title_link":${BUILD_URL},"text":"Selfservice-API build details:","image_url":"https://i.imgflip.com/1czxka.jpg","color":"#e3211e"}]}'
//         common.rocketChatNotificaiton("${ROCKETCHAT_TOKEN}", "${ROCKETCHAT_CHANNEL}", "${FAILED_COMMENT}" )
//         throw error
//       }
//     }
//   }
// }

// // Deploying WEB to Dev
// stage("Deploy" + WEB_IMAGESTREAM_NAME + "to ${common.web_environments.dev.name}") {
//   def environment = common.web_environments.dev.tag
//   def url = common.web_environments.dev.url
//   node{
//     try{
//       common.deployAndVerify(WEB_IMAGE_HASH,environment,WEB_IMAGESTREAM_NAME)

//       // WEB Deployment Success notification
//       COMMENT = '{"username":"bcsc-jedi","icon_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTizwY92yvdrPaFVBlbw6JW9fiDxZrogj10UvkKGnp66xLNx3io5Q&s","text":"SelfService-UI Deployment Success 🚀","attachments":[{"title":"Selfservice-ui Deployment","title_link":${BUILD_URL},"text":"Selfservice-ui build details:","image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwc_SWm-J_9OPSJVzUqxibPHZI55EBwpOB-JPeY0drU64YENdUWA&s","color":"#1ee321"}]}'
//       ROCKETCHAT_TOKEN = sh (
//                     script: """oc get secret/rocketchat-token-secret -n ${NAMESPACE_BUILD} -o template --template="{{.data.ROCKETCHAT_TOKEN}}" | base64 --decode""",
//                         returnStdout: true).trim()
//       common.rocketChatNotificaiton("${ROCKETCHAT_TOKEN}", "${ROCKETCHAT_CHANNEL}", "${COMMENT}" )
//     }catch(error){
//       // Web Deployment Failure Notification
//       FAILED_COMMENT = '{"username":"bcsc-jedi","icon_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTizwY92yvdrPaFVBlbw6JW9fiDxZrogj10UvkKGnp66xLNx3io5Q&s","text":"SelfService-UI Deployment Failure 🤕","attachments":[{"title":"Selfservice-ui Deployment","title_link":${BUILD_URL},"text":"Selfservice-ui build details:","image_url":"https://i.imgflip.com/1czxka.jpg","color":"#e3211e"}]}'
//       common.rocketChatNotificaiton("${ROCKETCHAT_TOKEN}", "${ROCKETCHAT_CHANNEL}", "${FAILED_COMMENT}" )
//       throw error
//     }
//   }
// }

// // Deploying DB to Dev
// stage("Deploy to" + DB_NAME + "${common.db_environments.dev.name}") {
//   def environment = common.db_environments.dev.tag
//   def url = common.db_environments.dev.url
//   node{
//     try{
//       common.deployAndVerify(DB_IMAGE_HASH,environment,DB_IMAGESTREAM_NAME)

//       // DB Deployment Success notification
//       COMMENT = '{"username":"bcsc-jedi","icon_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTizwY92yvdrPaFVBlbw6JW9fiDxZrogj10UvkKGnp66xLNx3io5Q&s","text":"SelfService-DB Deployment Success 🚀","attachments":[{"title":"Selfservice-db Deployment","title_link":"${BUILD_URL}","text":"Selfservice-DB Deployment details:","image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwc_SWm-J_9OPSJVzUqxibPHZI55EBwpOB-JPeY0drU64YENdUWA&s","color":"#1ee321"}]}'
//       ROCKETCHAT_TOKEN = sh (
//                     script: """oc get secret/rocketchat-token-secret -n ${NAMESPACE_BUILD} -o template --template="{{.data.ROCKETCHAT_TOKEN}}" | base64 --decode""",
//                         returnStdout: true).trim()
//       common.rocketChatNotificaiton("${ROCKETCHAT_TOKEN}", "${ROCKETCHAT_CHANNEL}", COMMENT )
//     }catch(error){
//       // DB Deployment Failure notification
//       FAILED_COMMENT = '{"username":"bcsc-jedi","icon_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTizwY92yvdrPaFVBlbw6JW9fiDxZrogj10UvkKGnp66xLNx3io5Q&s","text":"SelfService-UI Deployment Failure 🤕","attachments":[{"title":"Selfservice-db Deployment","title_link":"${BUILD_URL}","text":"Selfservice-DB Deployment details:","image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWWlY9blSXitK3hnPaxoUlZPiV3oJRcGrq3STQDwKsExo4bmgP&s","color":"#e3211e"}]}'
//       common.rocketChatNotificaiton("${ROCKETCHAT_TOKEN}", "${ROCKETCHAT_CHANNEL}", "${FAILED_COMMENT}" )
//       throw error
//     }
// }
// }

// // Deploying DB to Dev
// stage("Deploy to" + API_NAME + "${common.api_environments.dev.name}") {
//   def environment = common.api_environments.dev.tag
//   def url = common.api_environments.dev.url
//   node{
//     try{
//       common.deployAndVerify(API_IMAGE_HASH,environment,API_IMAGESTREAM_NAME)

//       // DB Deployment Success notification
//       // COMMENT = '{"username":"bcsc-jedi","icon_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTizwY92yvdrPaFVBlbw6JW9fiDxZrogj10UvkKGnp66xLNx3io5Q&s","text":"SelfService-API Deployment Success 🚀","attachments":[{"title":"Selfservice-API Deployment","title_link":"${BUILD_URL}","text":"Selfservice-API Deployment details:","image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwc_SWm-J_9OPSJVzUqxibPHZI55EBwpOB-JPeY0drU64YENdUWA&s","color":"#1ee321"}]}'
//       ROCKETCHAT_TOKEN = sh (
//                     script: """oc get secret/rocketchat-token-secret -n ${NAMESPACE_BUILD} -o template --template="{{.data.ROCKETCHAT_TOKEN}}" | base64 --decode""",
//                         returnStdout: true).trim()
//       common.rocketChatNotificaiton("${ROCKETCHAT_TOKEN}", "${ROCKETCHAT_CHANNEL}", API_IMAGESTREAM_NAME )
//     }catch(error){
//       // DB Deployment Failure notification
//       FAILED_COMMENT = '{"username":"bcsc-jedi","icon_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTizwY92yvdrPaFVBlbw6JW9fiDxZrogj10UvkKGnp66xLNx3io5Q&s","text":"SelfService-API Deployment Failure 🤕","attachments":[{"title":"Selfservice-API Deployment","title_link":"${BUILD_URL}","text":"Selfservice-API Deployment details:","image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWWlY9blSXitK3hnPaxoUlZPiV3oJRcGrq3STQDwKsExo4bmgP&s","color":"#e3211e"}]}'
//       common.rocketChatNotificaiton("${ROCKETCHAT_TOKEN}", "${ROCKETCHAT_CHANNEL}", "${FAILED_COMMENT}" )
//       throw error
//     }
//   }
// }  