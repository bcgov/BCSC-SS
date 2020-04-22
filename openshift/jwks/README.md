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
    "kty": "RSA",
    "e": "AQAB",
    "use": "enc",
    "kid": "testkey",
    "alg": "RS256",
    "n": "t2MsTsJGRoMS4AlHX5uprzspq9g18c2DwVezuQSAeFcCy4BXECmLjmNbcaqLX4pDx48ht2fm5lNdd7vsL_1QDxUVxvHMtueMm9ZxbHYLyfWNC34aB6gHakVW4dX2km3-gKCKaZP_tDm8PvcO9uhpd2i3F3MerPR9JJrznwpMGbnYCEJlgaBTXeajZFbDqK5MwaWN1TwyL99cltWzBsj5qy2nlPfOQU4BHZtH7U4oBAOhM9kA6jbJZKoNKUWIVf4rgTi2FH5pHyz8yEP451xDTf6uxaR4jdMxLYAok-jgHNZxca9aMNekmpTY6SNFhDgoWUzNrmsDBs5WnxVLGqTBWw"
}
    ]
}

```
The corresponding private key file is in jwks-private.json , not sure how to use this right now ... 
Get these keys from the key generation site https://mkjwk.org/ 
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
