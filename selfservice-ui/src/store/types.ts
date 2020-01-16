import { KeyCloakState } from './modules/KeyCloak/types';
export interface RootState {
  version: string;
  KeyCloakModule: KeyCloakState;
}
