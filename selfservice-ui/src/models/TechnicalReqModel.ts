export interface TechnicalReqModel {
  id?: string;
  projectId: string;
  clientUri: string;
  redirectUris: string[];
  jwksUri: string;
  idTokenSignedResponseAlg: string;
  userinfoSignedResponseAlg: string;
}
