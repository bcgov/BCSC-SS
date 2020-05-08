const signedAlgorithm = [
  'RS256',
  'RS384',
  'RS512',
  'ES256',
  'ES384',
  'ES512',
  'PS256',
  'PS384',
  'PS512',
];

const encryptedAlgorithm = ['RSA1_5', 'RSA-OAEP'];

const encryptedEncoding = [
  'A256GCM',
  'A256CBC+HS512',
  'A192GCM',
  'A128GCM',
  'A128CBC-HS256',
  'A192CBC-HS384',
  'A256CBC-HS512',
  'A128CBC+HS256',
];

export { signedAlgorithm, encryptedAlgorithm, encryptedEncoding };
