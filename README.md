# BCSC-SS
Resources to make it easier for public organizations to offer the widely used BC Services Card a secure and verified government issued identity card as a login option for online services.

[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-white.svg)](https://sonarcloud.io/dashboard?id=bcgov_BCSC-SS)


[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=bcgov_BCSC-SS&metric=alert_status)](https://sonarcloud.io/dashboard?id=bcgov_BCSC-SS)
![BCSC_SS API integration tests](https://github.com/bcgov/BCSC-SS/workflows/BCSC_SS%20API%20integration%20tests/badge.svg)
![BCSC_SS UI tests](https://github.com/bcgov/BCSC-SS/workflows/BCSC_SS%20UI%20tests/badge.svg)

# License

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

## Introduction

Our vision: Make it easier for public organizations to offer the widely used BC Services Card, a secure and verified government issued identity as a login option for online services. 

## Repo Structure

```
.
├── CODE_OF_CONDUCT.md
├── COMPLIANCE.yaml
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── jenkins
├── local
├── openshift
├── selfservice-api
├── selfservice-db
├── selfservice-ui
└── sonar-runner
```


* `selfservice-api`: Selfservice-api is an python application and runs a backend functionality and will be an dockerized application. API directory consists Dockerfile, flask api, tests.
  ## Technology Stack
  * Python, Flask
  * Postgres - SQLAlchemy, psycop2-binary & alembic

* `selfservice-ui`: Selfservice-UI is a frontend Vue application exposed over https:443.
  ## Technology Stack
  * Vue, Vuex, Vuetify, webpack, vue-i18n
  * Styleguidist, keycloak-js, babel
  * Jest, Istanbul
  
* `openshift`: openshift folder consists holds all the openshift templates for deploying buildConfigs, deploymentConfigs, Pipeline buildConfigs, configMaps, secretMaps and network policies.  
    ```
    ./openshift
    ├── network_policies
    │   ├── nsp_dev.yaml
    │   ├── nsp_test.yaml
    │   └── nsp_tools.yaml
    ├── selfservice-api
    │   ├── api-build.yaml
    │   ├── api-deploy-configmap.yaml
    │   ├── api-deploy-test.yaml
    │   ├── api-deploy.yaml
    │   └── api-pipeline.yaml
    ├── selfservice-db
    │   ├── db-build.yaml
    │   ├── db-deploy-configmap.yaml
    │   ├── db-deploy-test-Ephemeral.yaml
    │   ├── db-deploy.yaml
    │   └── db-pipeline.yaml
    ├── selfservice-ui
    │   ├── bcsc-pipeline.yaml
    │   ├── jenkins
    │   ├── secretmap_sample.yaml
    │   ├── web-build-configmap.yaml
    │   ├── web-build.yaml
    │   ├── web-build_test.yaml
    │   └── web-deploy.yaml
    └── sonarqube
        ├── sonarqube-postgresql-template.yaml
        └── sonarqube.md
    ```

* `jenkins`: Jenkins folder holds pipeline code (jenkinsfile) for webhook triggered deployment based on merge and to their respective branch.
    ```
    ./jenkins
    ├── jenkinsfile.common.groovy
    ├── jenkinsfile.db.groovy
    ├── jenkinsfile.dev.groovy
    ├── jenkinsfile.prod.groovy
    └── jenkinsfile.test.groovy
    ```

* `local`: Folder holds docker-compose files and bash scripts to deploy complete BC Service card application solution locally.

    ```
    ./local
    ├── docker-compose-db.yml
    ├── docker-compose.yml
    ├── ready_local_db.sh
    ├── start.sh
    └── stop.sh
    ```
* `.github`: Directory holds github Actions workflow for frontend and API unit and integration testing respectively. Actions will trigger on pull request to respective branch and initiate testing before merge and if test fails, it will break the merge process. 


##  Deployment
We will be using this Github repository as our input source code repository and
deploy  BCSC application to multiple environments to Local (Docker Compose) and openshift through the Jenkins pipeline.

## Local

#### Prequisites

  * As prerequistes for local deployment, you require docker and docker-compose and git cli. Please follow links to install instructions.
  * Docker Installation: [Docker installation Instructions](https://docs.docker.com/compose/install/)
  * Docker Compose Installation: [Docker Compose Instructions](https://docs.docker.com/compose/install/)
  * Git Installation: [Git Installation Instructions](https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/)
    
  For local deployment, clone the github repository and change the `start.sh` and `stop.sh` permissions to executable and run the start,sh to setup local environment.

  Follow below steps:

  ```
  git clone https://github.com/AOT-Technologies/vue-node-template.git
  cd deployment/local/
  chmod +x *.sh
  
  # Will bring your application up and open local application URL in browser
  sh start.sh   

  # To shutdown the application
  sh stop.sh
  ```


##  Deployment
We will be using this Github repository as our input source code repository and
deploy  code challenge project to multiple environments to Local (Docker Compose), AWS and openshift through the different CI Platforms as AWS CodePipeline and Jenkins pipeline.

## Local

#### prerequisites

  * As prerequistes for local deployment, you require docker and docker-compose and git cli. Please follow links to install instructions.
  * Docker Installation: [Docker installation Instructions](https://docs.docker.com/compose/install/)
  * Docker Compose Installation: [Docker Compose Instructions](https://docs.docker.com/compose/install/)
  * Git Installation: [Git Installation Instructions](https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/)
    
  For local deployment, clone the github repository and change the `start.sh` and `stop.sh` permissions to executable and run the start,sh to setup local environment.

  Follow below steps:

  ```
  git clone https://github.com/AOT-Technologies/vue-node-template.git
  cd deployment/local/
  chmod +x *.sh
  
  # Will bring your application up and open local application URL in browser
  sh start.sh   

  # To shutdown the application
  sh stop.sh
  ```

## Openshift

####  Pipeline Architecture

`Please update Architecture`

#### prerequisites

* As a prerequisites for openshift deployment , you require openshft oc-cli or kubectl. Please follow below instruction to install.
* Openshift Cli Installation: [Openshift Cli installation instructions](https://docs.openshift.com/enterprise/3.1/cli_reference/get_started_cli.html)
*  Kubectl Installation: [Kubectl installation instruction](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

#### Deployment Instructions

* Step 1: apply netwrok security policies as pathfinder platform deny all traffic by default even within openshift project (namespace). 
    ```
    cd opensshift/network_policies
    oc login 
    oc apply -f nsp_tools.yaml -n oultzp-tools
    oc apply -f nsp_dev.yaml -n oultzp-dev
    oc apply -f nsp_test.yaml -n oultzp-test
    oc apply -f nsp_prod.yaml -n oultzp-prod
    ```
* Step 2: Install buildConfig in the tools namespace.
    ```
    cd openshift
    oc process -f ./selfservice-ui/web-build.yaml | oc apply -n oultzp-tools -f -
    oc process -f ./selfservice-api/api-build.yaml | oc apply -n oultzp-tools -f -
    oc process -f ./selfservice-db/db-build.yaml | oc apply -n oultzp-tools -f -
    ```
* Step 3: Install Deployment Configs, ConfigMap's, SecretMaps & pipeline buildConfig in the dev, test & prod environment respectively.
    ```
    cd openshift

    -- Web deployment --
    oc process -f ./selfservice-ui/web-build-configmap.yaml -p dev-ui.env | oc apply -n oultzp-dev -f -
    oc process -f ./selfservice-ui/web-secretmap.yaml -p dev-ui.env | oc apply -n oultzp-dev -f -
    oc process -f ./selfservice-ui/web-deploy.yaml -p dev-ui.env | oc apply -n oultzp-dev -f -

    -- DB Deployment --
    oc process -f ./selfservice-db/db-deploy-configmap.yaml -p dev-db.env | oc apply -n oultzp-dev -f -
    oc process -f ./selfservice-db/db-deploy.yaml -p dev-db.env | oc apply -n oultzp-dev -f -

    -- API Deployment
    oc process -f ./selfservice-api/api-deploy-configmap.yaml -p dev-api.env | oc apply -n oultzp-dev -f -
    oc process -f ./selfservice-api/api-deploy.yaml -p dev-api.env | oc apply -n oultzp-dev -f -
    ```

* Step 4: Deploy pipeline build config for dev,test & prod in tools namestace.
  ```
    cd openshift
    oc process -f ./selfservice-ui/bcsc_pipeline.yaml -p dev-pipeline.env| oc apply -n oultzp-tools -f -
    oc process -f ./selfservice-ui/bcsc_pipeline.yaml -p test-pipeline.env| oc apply -n oultzp-tools -f -
    oc process -f ./selfservice-ui/bcsc_pipeline.yaml -p prod-pipeline.env| oc apply -n oultzp-tools -f -
  ```