export interface KeyCloakState {
  keycloakAuth?: object;
  authenticated: boolean;
  token: string;
  loading?: boolean;
  profile: [];
  isAdmin: boolean;
  isClient: boolean;
  isVerfied: boolean;
  fields: [];
  provider: string;
  errorStatus: boolean;
  successStatus: boolean;
  profileErrorStatus: boolean;
  emailExistErrorStatus: boolean;
}
