export interface TechnicalReqModel {
  id?: number;
  projectId?: number;
  clientUri: string;
  redirectUris: string[];
  jwksUri: string;
  encryptedResponseAlg: string;
  signedResponseAlg: string;
}
