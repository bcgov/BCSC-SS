# Database Backups

This project implements the [BCDevOps/backup-container](https://github.com/BCDevOps/backup-container) containerized backup solution.

It is not a part of any deployment pipeline and is deployed manually. The process to deploy manually proceeds as follows:

 1. In the deployment project, prepare a nfs-backup volume as directed at the following https://github.com/BCDevOps/provision-nfs-apb

 2. The repository should these files and directories, which are available at [BCDevOps/backup-container](https://github.com/BCDevOps/backup-container):
  - `./openshift/backup` contains `backup-build.json`, `backup-cronjob.json`, and `backup-deploy.json`.
  - `./openshift/config/backup.conf`.

 3. build the base image into the `tools` namespace
  - `oc project <tools-namespace>`
  - `oc process -f backup-build.json | oc create -f -`

 4. tag the latest image with a <env> tag -> this does not accidentally trigger deployment when updating the image
  - `oc tag backup:latest backup:dev  # this may be repeated to create more tags from this build`

 5. Manually list the database(s) and desired cron schedule(s) into `./openshift/config/backup.conf` as (or similar):
  - `<Hostname/>:<Port/>/<DatabaseName/>`
  - `0 9 * * * default ./backup.sh -s  # the backup schedule`
  - `0 12 * * * default ./backup.sh -s -v all  # the verification schedule`

 6. Run `./backup-deploy.overrides.sh` to create two files:
  - `backup-conf-configmap_DeploymentConfig.json`, which is a configuration file to be deployed as a ConfigMap; and,
  - `backup-deploy.overrides.param`, which will be passed as a `--param-file` to process the `backup-deploy.json` deployment creation.

 7. Switch projects to your intended deployment project.<sup>\*</sup>
  - `oc project <deployment-namespace>`

 8. Create the ConfigMap using the template created in the last step.
  - `oc create -f backup-conf-configmap_DeploymentConfig.json`

 9. The `backup-deploy.overrides.param` should contain the following:

 ```
 #=========================================================
 # OpenShift template parameters for:
 # Component: backup
 # Template File: backup/backup-deploy.json
 #=========================================================
 NAME=backup
 SOURCE_IMAGE_NAME=backup
 IMAGE_NAMESPACE=<tools_projectname>
 TAG_NAME=<tag>  # latest, or whatever was tagged in step #4
 # deployment backup details and s trategy
 # database access
 DATABASE_DEPLOYMENT_NAME=<database-secret-name>
 DATABASE_USER_KEY_NAME=<db-username-key>  # the database secret's username key
 DATABASE_PASSWORD_KEY_NAME=<db-password-key>  # the database secret's password key
 # database backup strategy settings
 # reference: https://github.com/BCDevOps/backup-container#backup-strategies
 BACKUP_STRATEGY=daily  # defaults to rolling if empty
 BACKUP_DIR=/backups/
 NUM_BACKUPS=30  # only used by daily strategy
 DAILY_BACKUPS=0  # only used by rolling strategy
 WEEKLY_BACKUPS=0  # only used by rolling strategy
 MONTHLY_BACKUPS=0  # only used by rolling strategy
 BACKUP_PERIOD=1d  # only used by legacy mode
 # configuration and backup and verifcation volumes
 CONFIG_MAP_NAME=backup-conf  # the ConfigMap name (default: backup-conf)
 CONFIG_FILE_NAME=backup.conf  # as created in the ConfigMap (default: backup.conf)
 CONFIG_MOUNT_PATH=/
 BACKUP_VOLUME_NAME=<bk-projectname-nfsid>  # set this to the preconfigured nfs-backup volume id from step 1
 BACKUP_VOLUME_SIZE=1Gi
 BACKUP_VOLUME_CLASS=nfs-backup
 VERIFICATION_VOLUME_NAME=backup-verification
 VERIFICATION_VOLUME_SIZE=5Gi
 VERIFICATION_VOLUME_CLASS=gluster-file-db
 VERIFICATION_VOLUME_MOUNT_PATH=/var/lib/pgsql/data
 # resources
 CPU_REQUEST=0
 CPU_LIMIT=0
 MEMORY_REQUEST=0Mi
 MEMORY_LIMIT=0Mi
 # optional webhook integration (intended primarily for a Rocket.Chat plugin):
 # reference: https://github.com/BCDevOps/backup-container#using-the-webhook-integration
 WEBHOOK_URL=
 ENVIRONMENT_FRIENDLY_NAME=
 ENVIRONMENT_NAME=
 ```

 10. process and create the backup deployment, injecting parameters using the overrides file from the step above:
  - `oc process -f backup/backup-deploy.json --param-file=backup-deploy.overrides.param -o yaml | oc create -f -`

<sup>\*</sup> note that since the build artifact is in the `tools` project, the expectation is a `system:serviceaccounts:<project-namespace>` having the `system:image-puller` tag must exist. This is already the case if a pipeline as used in the `CAPS` project.