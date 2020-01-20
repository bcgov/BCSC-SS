import { KeyCloakState } from './modules/KeyCloak/types';
export interface RootState {
  ProjectInfoModule: any;
  version: string;
  KeyCloakModule: KeyCloakState;
}
