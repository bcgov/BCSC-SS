# JWKS Readme

 This is a build of a really simple nginx docker container which provides a jwks.json file from a URL for JWT encryption purposes

 You can build it using docker or docker compose
 You need to set the environment variables in Dockerfile (for Docker) or jwks_nginx.yaml (for docker-compose) to match your server host name and the port nginx is listening to.
 They are

 `JWKS_SERVER_PORT` - default is 80 (note we map this port to 8083 - of course you can change this too )
 `JWKS_SERVER_NAME` - default is localhost

 ## Docker  commands
 ### build
 `docker build -t nginx-jwks .`
 ### run
 `docker run --name nginx-jwks  -p 8083:80 nginx-jwks`

 ## Docker Compose commands
 ### build and run 
 `docker-compose  -f jwks_nginx.yaml up`

 ## Operation

 http://localhost:8083 will just return the jwks.json which you have in the local directory.

 ## Encryption
 Note the format of the jwks.json
 ```
{ "keys" : [
{
  "use": "enc",
  "kty": "RSA",
  "kid": "bcsc-demo",
  "alg": "RSA-OAEP",
  "n": "nY-t_UNF_ItsrDbHzBrI9bNfhj0B4YBTlHIsiP3m1BYUgcokSmM_YYilT_QP8exNHrYYHk7XD2cISZSGANibIxAHNNwv8CVXN6uL2R1mly5QupadmFhFMjq2JOzr972w2aUs0NO9dQ1lPk_A6w9T8QYoLti8ChT2ColmJDs3PHbFTSG0C9DX1_FE8aVYOE-SQYqzY5unOkjCD_3kYt6HT3tsTc5ZPoB8jSgAcQ-Q2SYu5-KArZQtghbeXP25GFPoIN-z6-UuPZI70v-1FodzCqW721B3Xk577N7r8a7KAcFUb6eYPAtGh7GFJBUCNpo4etL51LSb7dWFZnWDlODNgQ",
  "e": "AQAB"
}
    ]
}

```
The corresponding private key file is in jwks-private.json, normally this would NOT be publically available in plugged into the application requesting the encrypted JWTs (see the demo apps). But for this sample it's OK as it ONLY should be used for test/demo purposes and ONLY in the test environment.

To generate this file, install a great utility called step from [https://smallstep.com/docs/cli/crypto/jwk/create/!smallstep].

The instructions for Windows aren't clear, I just downloaded step_windows_0.14.4-rc.1_amd64.tar.gz and unzipped using the bash shell provided by git bash 

tar xzf step_windows_0.14.4-rc.1_amd64.tar.gz
Then cd to the directory where the step.exe is and run

$ ./step crypto jwk create c:/Users/chris/pub.jwk c:/Users/chris/priv.jwk -kty=RSA -size=2048 -alg=RSA-OAEP -use=enc -kid=bcsc-demo -no-password -insecure

NB: Important that the alg matches that which you plug into the BCSC-SS app encryption algorithm !!!!

Then cut and paste this JWK into a JWKS file (basically add the {keys: []} array around the key )


## OpenShift

## Setting up builds and deployments

1. Upload `jwk-build.yaml` to the `tools` environment
2. Upload `jwk-deploy.yaml` to the dev/test/prod/whatever environment.  Currently we only are deploying to test.

Make sure you update the environment variables as appropriate to each environment.

 
## Deploying a build

Deploying the latest JWKS code is simple.  We do not use a Jenkins pipeline here.

1. Login to OpenShift and navigate to the  "tools" project
2. Builds > Builds, then select `jwks-build-test`
3. Click 'Start Build' in the top right.

This will trigger a build, which takes ~2-5 minutes, and then after that a deployment in the TEST environment (another 1-2 mins).  Then the deployment should be complete and the changes should be updated at `https://services-card-jwks-demo.pathfinder.gov.bc.ca/`
