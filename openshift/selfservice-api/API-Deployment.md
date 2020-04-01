# Selfservice-API Enviroment

## Cleanup


* `API Deployment Deletion:`

    * Dev
    ```
    oc process -f api-deploy.yaml --param-file=param/dev_api_deploy.env | oc delete -f - -n oultzp-dev
    ```
    * Test
    ```
    oc process -f api-deploy.yaml --param-file=param/test_api_deploy.env | oc delete -f - -n oultzp-test
    ```
    
    * Prod
    ```
    oc process -f api-deploy.yaml --param-file=param/prod_api_deploy.env | oc delete -f - -n oultzp-prod
    ```
* `API ConfigMap Deletion:`

    * Prod/Test/Dev
    ```
    oc process -f api-deploy-configmap.yaml | oc delete -f - -n oultzp-prod
    ```

* `API DB ConfigMap Deletion:`

    * Dev
    ```
    oc process -f db-deploy-configmap.yaml --param-file=param/dev_db_config.env | oc delete -f - -n oultzp-dev
    ```
    * Test
    ```
    oc process -f db-deploy-configmap.yaml --param-file=param/test_db_config.env | oc delete -f - -n oultzp-test
    ```
    
    * Prod
    ```
    oc process -f db-deploy-configmap.yaml --param-file=param/prod_db_config.env | oc delete -f - -n oultzp-prod
    ```

## API Deployment

* `API ConfigMap Deploy:`

    * Prod/Test/Dev
    ```
    oc process -f api-deploy-configmap.yaml | oc apply -f - -n oultzp-prod
    ```

* `API DB ConfigMap Deploy:`

    * Dev
    ```
    oc process -f db-deploy-configmap.yaml --param-file=param/dev_db_config.env | oc apply -f - -n oultzp-dev
    ```
    * Test
    ```
    oc process -f db-deploy-configmap.yaml --param-file=param/test_db_config.env | oc apply -f - -n oultzp-test
    ```
    
    * Prod
    ```
    oc process -f db-deploy-configmap.yaml --param-file=param/prod_db_config.env | oc apply -f - -n oultzp-prod
    ```

* `API Deployment Deploy:`

    * Dev
    ```
    oc process -f api-deploy.yaml --param-file=param/dev_api_deploy.env | oc apply -f - -n oultzp-dev
    ```
    * Test
    ```
    oc process -f api-deploy.yaml --param-file=param/test_api_deploy.env | oc apply -f - -n oultzp-test
    ```
    
    * Prod
    ```
    oc process -f api-deploy.yaml --param-file=param/prod_api_deploy.env | oc apply -f - -n oultzp-prod