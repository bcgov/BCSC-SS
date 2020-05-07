export interface TechnicalReqModel {
  id?: number;
  projectId?: number;
  clientUri: string;
  redirectUris: string[];
  jwksUri: string;
  encryptedResponseEnc: string | null;
  encryptedResponseAlg: string | null;
  signedResponseAlg: string | null;
  signingEncryptionType: number;
}
