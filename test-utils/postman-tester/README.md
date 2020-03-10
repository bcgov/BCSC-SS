# BCSC-Postman OAuth 2.0
A Postman collection for authenticating to the BCSC API. 

## Steps to get up and running
Follow these steps to quickly test out your access to the BC Services Card OIDC environment

### 1. Get an OAuth2 (OIDC)  key and secret for your application from the BC Services Card Self Service site
Lets assume that these are called "Client key" and "Client secret". Remember your redirect URL "Redirect URL" and the scopes you have requested. You also need to remember whether you are encrypting or signing  the response or whether you require the response in JWT or JSON format . The signing parameters (id_token_signed_response_alg,  userinfo_signed_response_alg) are linked to the JWKS URL and the encryption parameters (id_token_encrypted_reponse and userinfo_encrypted_response ) determine whether the response is encrypted. 

### 2. Import the BCSC OAuth 2.0 collection and BCSC environment into Postman
Click the button below and select the Desktop version of Postman (Chrome extension doesn't support environment variables). This will also install the Collection and Environment we'll be using.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/715f6c5fd3d4ce3511f9)

Alternatively, you can download the BCSC OAuth2.0.postman_collection and BCSC 2.0.postman_environment JSON files above and import them via the Import button in the top left of the Postman Workplace sceen.

### 3. Add your environment variables in Postman
Copy your Client id, Client secret, redirect URI and scopes from the BC Services Card Self Service site into the environment variables in Postman.
The mapping is as follows : 
```
Client id -> client_id
Client secrect -> client_secret
Redirect URI -> redirect_uri
Scopes -> scope
```

 To add these details to the Environment, make sure you have the "BCSC OAuth 2.0" Environment selected in Postman, click the eye button, then edit.

![Environment with some details](images/setenv.PNG)

### 4. Test that your client id and redirect url are ok
1. Click on the "Basic Authorise Test" GET request under the BCSC OAuth 2.0 Collection
1. Click "Send"
1. Click on the Test Results tab

You should get a response with a green "Pass" logo . If it fails you will get a bunch of red html, you may be able to determine what the cause is, most likely your Client Id is wrong or your Redirect URL is incorrect.

![Basic Authorize Test](images/basic-auth-test.PNG)


### 5. Do a full test by getting your user attributes (NB. You will need a test account which you should have received from the BC Services Card Self Service site )

1. Click on the "GET Attributes" request under the BCSC OAuth 2.0 Collection
1. Select the tab "Authorisation" . Ensure that the Type is set to OAuth 2.0
1. Click on the "Get new Access Token" button

![Basic Authorize Test](images/Attributes.PNG)


Add values for each of the fields as follows (yes, type the curly brackets too ) :

```
Token Name : mytoken
Grant Type : Authorization Code
Callback URL : {{redirect_uri}}
Auth URL : {{authURI}}
Access Token URL :  {{accessTokenURI}}
Client ID : {{client_id}}
Client Secret : {{client_secret}}
Scope : {{scope}}
State : 1234
Client Authentication :  Send as Basic Auth header
```

Note : For each of the fields presented (the {{...}} gets replaced by the variables you have already defined in step 3 above )  - and this is remembered so that you can simply change your environment if necessary without redoing the current step.



Once done, you can click "Request Token" and if all is well , you will be redirected to the standard login screens requesting your BCSC credentials.Using your test account data as a virtual card login, complete the login steps.

![BCSC Login 1](images/bcsc_login_1.PNG)
![BCSC Login 2](images/bcsc_login_2.PNG)
![BCSC Login 3](images/bcsc_login_3.PNG)
![BCSC Login 4](images/bcsc_login_4.PNG)



 If all goes well, you will be returned a token 



![Successful access token](images/access_token_return.PNG)

Now the fun part - simply click on "Send" for the request and you should get your user attributes returned - note that postman automatically adds your access token returned in the previous step , so you do not need to add anything manually to the GET request header. 

![Get your attributes](images/get_attributes.PNG)


Note: Depending on your encryption settings which you set up in the BC Services Card Self Service application, the attributes returned could be encrypted, returned as a JWT token or returned as JSON. 

Note : To see the contents of a JWT token you can decode using eg.  https://jwt.io 

You can verify that the data returned is the same as that displayed during the BC Services Card login process, and that the scopes are limited to those set up in your BC Services Card Self Service application

