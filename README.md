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

./local
├── docker-compose-db.yml
├── docker-compose.yml
├── ready_local_db.sh
├── start.sh
└── stop.sh
```


* `selfservice-api`: Selfservice-api is an python application and runs a backend functionality and will be an dockerized application. API directory consists Dockerfile, flask api, tests.
  ## Technology Stack
  * Python, Flask
  * Postgres - SQLAlchemy, psycop2-binary & alembic
* `selfservice-ui`: Frontend Vue application exposed over http:80. Directory consists of Dockerfile, buildspec_web.yml for AWS Codebuild and frontend application code.
  
* `openshift`: This directory contains local deployment sub-directory and aws sub-directory with set of cloudformation template to create codepipline, codebuild, ECR repository for docker image, VPC based fargate cluster for docker based deployment. Additionaly, for easy deployment there is another file `cfn-cli.yml` for ordered infrasturcure provisioning.




SELECT * FROM information_schema.tables WHERE table_schema='public'

psql -h selfservice-db.oultzp-dev.svc -d postgres -U postgres