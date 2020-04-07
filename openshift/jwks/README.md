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
			{"kty":"RSA",
			"e":"AQAB",
			"kid":"dummy",
			"alg" : "RS256", 
			"use" : "enc",
			"n":"uks-oR3vXWIet4rUKSMnOi8cof2APJUyDAmFOfaYLCpC7tt_ogHhH0BrQmXKSgDeU5MQN30F1cb1yZLdbctoaJD1FmyhgP7dq6Y5ByZZPojW2rlo9wmpNV6Sji3YsvMgSKMtWXUXQ1bWz9cG8SLYeJt4XflJlUjGh0qjWLk6hgXnEIx-UTzcWTApE51uFf_8WxVDIb2cb0dFl1Z5KX7ZbBwkPd1RNdZNOwUaaChq1OwI02B53dYO85SKLGUL0mTl5vis_hEzjhCDq_l3zsLO_oSIcxk0XUfPfTBGzsFd4DOi-TE7dzNqK7UiKqM7v-bKg5eU_4gKeyFnOnZwBPPpqw"
			}
    ]
}
```
The only value which can be changed is the "n" property which is the public key obtained from demojwks.cert.pem , converted from the PEM format in this file to the JWKS modulo format using an online tool eg. https://8gwifi.org/jwkconvertfunctions.jsp

 
