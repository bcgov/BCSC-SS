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

const encryptedAlgorithm = ['RSA1_5'];

const encryptedEncoding = ['A256GCM', 'A256CBC-HS512'];

export { signedAlgorithm, encryptedAlgorithm, encryptedEncoding };
