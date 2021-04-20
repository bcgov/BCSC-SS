# OC3 to OC4 Migration Notes


## Templates


### Patroni
- Patroni has been deployed using templates from BCDevOps/platform-services repository: https://github.com/BCDevOps/platform-services/tree/master/apps/pgsql/patroni/openshift
- Replaced old patroni templates with these updated templates in the openshift/patroni directory
- Updated PostgreSQL secrets containing database name and credentials can be found in each namespace `patroni-persistent-creds` (dev/test/prod namespaces) and `patroni-persistent-demo-creds` (in test namespace)
- In order to run psql commands, open interactive terminal in one of the `patroni-persistant-#` pods (or `patroni-persistant-demo-#`) and launch `psql` command along with specifying the name of the database. (database name is specified in patroni secret as `app-db-name`):

```shell
# ee5243-dev / pods / patroni-persistant-0 / terminal
$ psql -d bcscss

# ee5243-test / pods / patroni-persistant-0 / terminal
$ psql -d bcscss_test

# ee5243-test / pods / patroni-persistant-demo-0 / terminal
$ psql -d bcscss_demo    

# ee5243-prod / pods / patroni-persistant-0 / terminal
$ psql -d bcscss_prod    
```

## Upgrades/Updates
- **Dockerfiles have been updated**
  - `selfservice-api`:
    - Dockerfile has been updated to use a Python 3.9 image maintained by Bitnami and hosted by Amazon ECR Public Gallery
    - Bitnami images provide up to date bug fixes and security patches
    - repository: https://gallery.ecr.aws/bitnami/python
    - tag: `3.9-prod`
    - more information: https://github.com/bitnami/bitnami-docker-python
  - `selfservice-ui`:
    - Dockerfile has been updated to use a Node 12 image for build-stage, and nginx 1.18 for production-stage maintained by Bitnami and hosted by Amazon ECR Public Gallery
    - Bitnami images provide up to date bug fixes and security patches
    - repository: https://gallery.ecr.aws/bitnami/nginx
    - node tag: `12-prod`
    - nginx tag: `1.18`
    - more information: https://github.com/bitnami/bitnami-docker-nginx



## Vanity URLs
Secure routes have been created with vanity domains.

- dev: https://developer.iddev.gov.bc.ca/
- test: https://developer.idqa.gov.bc.ca/
- demo: https://developer.iddemo.gov.bc.ca/
- prod: https://developer.id.gov.bc.ca/



**Updating TLS Certificates**

Each route follows the following pattern. Certificates can be updated directly by editing the route's YAML in the OpenShift console.

*caCerticate is the Entrust l1k ca certificate and is valid until 2030.*

*Demo route name is `selfservice-ui-demo`*

  
```yaml
kind: Route
apiVersion: route.openshift.io/v1
metadata:
  name: selfservice-ui
  namespace: ee5243-[env]
  ...
  spec:
    host: developer.id[env].gov.bc.ca
    ...
    tls:
      termination: edge
      certificate: |-
      -----BEGIN CERTIFICATE-----
      certificate from `developer.id[env].gov.bc.ca.txt` file
      -----END CERTIFICATE-----
    key: |-
      -----BEGIN PRIVATE KEY-----
      private key from the original CSR request
      -----END PRIVATE KEY-----
    caCertificate: |
        -----BEGIN CERTIFICATE-----
        MIIFDjCCA/agAwIBAgIMDulMwwAAAABR03eFMA0GCSqGSIb3DQEBCwUAMIG+MQsw
        CQYDVQQGEwJVUzEWMBQGA1UEChMNRW50cnVzdCwgSW5jLjEoMCYGA1UECxMfU2Vl
        IHd3dy5lbnRydXN0Lm5ldC9sZWdhbC10ZXJtczE5MDcGA1UECxMwKGMpIDIwMDkg
        RW50cnVzdCwgSW5jLiAtIGZvciBhdXRob3JpemVkIHVzZSBvbmx5MTIwMAYDVQQD
        EylFbnRydXN0IFJvb3QgQ2VydGlmaWNhdGlvbiBBdXRob3JpdHkgLSBHMjAeFw0x
        NTEwMDUxOTEzNTZaFw0zMDEyMDUxOTQzNTZaMIG6MQswCQYDVQQGEwJVUzEWMBQG
        A1UEChMNRW50cnVzdCwgSW5jLjEoMCYGA1UECxMfU2VlIHd3dy5lbnRydXN0Lm5l
        dC9sZWdhbC10ZXJtczE5MDcGA1UECxMwKGMpIDIwMTIgRW50cnVzdCwgSW5jLiAt
        IGZvciBhdXRob3JpemVkIHVzZSBvbmx5MS4wLAYDVQQDEyVFbnRydXN0IENlcnRp
        ZmljYXRpb24gQXV0aG9yaXR5IC0gTDFLMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
        MIIBCgKCAQEA2j+W0E25L0Tn2zlem1DuXKVh2kFnUwmqAJqOV38pa9vH4SEkqjrQ
        jUcj0u1yFvCRIdJdt7hLqIOPt5EyaM/OJZMssn2XyP7BtBe6CZ4DkJN7fEmDImiK
        m95HwzGYei59QAvS7z7Tsoyqj0ip/wDoKVgG97aTWpRzJiatWA7lQrjV6nN5ZGhT
        JbiEz5R6rgZFDKNrTdDGvuoYpDbwkrK6HIiPOlJ/915tgxyd8B/lw9bdpXiSPbBt
        LOrJz5RBGXFEaLpHPATpXbo+8DX3Fbae8i4VHj9HyMg4p3NFXU2wO7GOFyk36t0F
        ASK7lDYqjVs1/lMZLwhGwSqzGmIdTivZGwIDAQABo4IBDDCCAQgwDgYDVR0PAQH/
        BAQDAgEGMBIGA1UdEwEB/wQIMAYBAf8CAQAwMwYIKwYBBQUHAQEEJzAlMCMGCCsG
        AQUFBzABhhdodHRwOi8vb2NzcC5lbnRydXN0Lm5ldDAwBgNVHR8EKTAnMCWgI6Ah
        hh9odHRwOi8vY3JsLmVudHJ1c3QubmV0L2cyY2EuY3JsMDsGA1UdIAQ0MDIwMAYE
        VR0gADAoMCYGCCsGAQUFBwIBFhpodHRwOi8vd3d3LmVudHJ1c3QubmV0L3JwYTAd
        BgNVHQ4EFgQUgqJwdN28Uz/Pe9T3zX+nYMYKTL8wHwYDVR0jBBgwFoAUanImetAe
        733nO2lR1GyNn5ASZqswDQYJKoZIhvcNAQELBQADggEBADnVjpiDYcgsY9NwHRkw
        y/YJrMxp1cncN0HyMg/vdMNY9ngnCTQIlZIv19+4o/0OgemknNM/TWgrFTEKFcxS
        BJPok1DD2bHi4Wi3Ogl08TRYCj93mEC45mj/XeTIRsXsgdfJghhcg85x2Ly/rJkC
        k9uUmITSnKa1/ly78EqvIazCP0kkZ9Yujs+szGQVGHLlbHfTUqi53Y2sAEo1GdRv
        c6N172tkw+CNgxKhiucOhk3YtCAbvmqljEtoZuMrx1gL+1YQ1JH7HdMxWBCMRON1
        exCdtTix9qrKgWRs6PLigVWXUX/hwidQosk8WwBD9lu51aX8/wdQQGcHsFXwt35u
        Lcw=
        -----END CERTIFICATE-----
      insecureEdgeTerminationPolicy: Redirect
    wildcardPolicy: None
```

## Deprecations and other notes
- Jenkins has been replaced entirely by build configurations
- Each build configuration along with image streams for selfservice-api and selfservice-ui have been deployed to separate environments (dev/test/prod)
- Backup Container has not been deployed as it has not been previously configured to save backups to external storage.
- JWKS demo container has been deployed in`ee5243-test` namespace
- The following template manifests in the BCSC-SS repo are now legacy and not being used, and can be deleted:
  ```
  .bcgov/BCSC-SS
  ...
  ├───openshift
  │   ├───backup-container
  │   ├───network_policies
  │   ├───selfservice-api
  │   ├───selfservice-db
  │   ├───selfservice-ui
  │   └───sonarqube
  ...
  ```