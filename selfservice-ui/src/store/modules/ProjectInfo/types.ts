import { ProjectInfoModel } from '@/models/ProjectInfoModel';
export interface ProjectInfoState {
  projectinfoList: ProjectInfoModel[];
  loading?: boolean;
  successStatus?: boolean;
  errorStatus?: boolean;
  singleProjectInfo: ProjectInfoModel[];
  message: string;
}
