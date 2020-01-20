import { KeyCloakState } from './modules/KeyCloak/types';
import { ProjectInfoState } from './modules/ProjectInfo/types';
export interface RootState {
  ProjectInfoModule: ProjectInfoState;
  version: string;
  KeyCloakModule: KeyCloakState;
}
