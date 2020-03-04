import { KeyCloakState } from './modules/KeyCloak/types';
import { ProjectInfoState } from './modules/ProjectInfo/types';
import { SharedState } from './modules/Shared/types';
export interface RootState {
  ProjectInfoModule: ProjectInfoState;
  version: string;
  KeyCloakModule: KeyCloakState;
  SharedModule: SharedState;
}
