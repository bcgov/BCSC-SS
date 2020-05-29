# Demo Environment

## Triggering a Build

The two builds (for api and ui) must both be triggered manually to update the demo environment.

In OpenShift "tools" project, go Builds > Builds.  Alternatively, you can click the hyperlinked names below to jump directly to the page.

1. Open up [selfservice-ui-build-demo](https://console.pathfinder.gov.bc.ca:8443/console/project/oultzp-tools/browse/builds/selfservice-ui-build-demo?tab=history)
2. Click "Start Build" in top right.
3. Repeat steps for [selfservice-api-build-demo](https://console.pathfinder.gov.bc.ca:8443/console/project/oultzp-tools/browse/builds/selfservice-api-build-demo?tab=history)

### Verifying it has been deployed

Builds should be automatically deployed after they are built, but to verify you can go to the ["Test" environment in Applications > Deployments](https://console.pathfinder.gov.bc.ca:8443/console/project/oultzp-test/browse/deployments).  We are looking at the "created" column for the deployments that end in "-demo".  The "created" value is when the latest deployment was, so it should be a recent (e.g. a few seconds/minutes ago depending on when you triggered the build)


## Modifying Builds

As of the writing of this document, the "demo" environment is configured to pull from the "test" branch on GitHub from the repo.  If one desires to modify it:

1. In OpenShift "tools" project, go Builds > Builds and find either the [selfservice-ui-build-demo](https://console.pathfinder.gov.bc.ca:8443/console/project/oultzp-tools/browse/builds/selfservice-ui-build-demo?tab=history) or [selfservice-api-build-demo](https://console.pathfinder.gov.bc.ca:8443/console/project/oultzp-tools/browse/builds/selfservice-api-build-demo?tab=history)
2. In top right, click "Actions > Edit"
3. On new screen, the top input should be Git Repository URL.  Click the "advanced options" text directly underneath it. 
4. Now the "git reference" field should be displayed.  Modify this field with the branch name (e.g. `master` / `test` / `dev`)