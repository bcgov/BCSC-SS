import { ProjectInfoModel } from '@/models/ProjectInfoModel';
export interface ProjectInfoState {
  projectinfoList: ProjectInfoModel[];
  loading?: boolean;
  successStatus?: boolean;
  errorStatus?: boolean;
  singleProjectInfo: ProjectInfoModel;
  message: string;
  finalErrorStatus?: boolean;
  finalSuccessStatus?: boolean;
  testAccountSuccess?: boolean;
  statusChangeError?: boolean;
  statusChangeSuccess?: boolean;
  deleteProjectError?: boolean;
  deleteProjectSuccess?: boolean;
  isCreated: boolean;
  isUpdated: boolean;
  history: any;
}
