# SonarQube template


rocketChatNotificaiton("${ROCKETCHAT_TOKEN}", "${ROCKETCHAT_CHANNEL}", "'{"username":"bcsc-jedi","icon_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTizwY92yvdrPaFVBlbw6JW9fiDxZrogj10UvkKGnp66xLNx3io5Q&s","text":"SelfService-UI build Success","attachments":[{"title":"Selfservice-ui build","title_link":"${currentBuild.absoluteUrl}/console","text":"Selfservice-ui build details:","image_url":"https://i.imgflip.com/1czxka.jpg","color":"#764FA5"}]}'" )