export interface TechnicalReqModel {
  id?: number;
  projectId?: number;
  clientUri: string;
  redirectUris: string[];
  jwksUri: string;
  idTokenSignedResponseAlg: string;
  userinfoSignedResponseAlg: string;
}
