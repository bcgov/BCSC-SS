import { TeamRoleModel } from '@/models/TeamRoleModel';

export interface TeamRoleState {
  teamRoles?: TeamRoleModel[];
  isLoading: boolean;
  successStatus?: boolean;
  errorStatus?: boolean;
  memberAdded?: boolean;
  memberAddedError?: boolean;
  memberAddedErrorList?: any;
  memberDetails: TeamRoleModel;
}
