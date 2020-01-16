export interface ProjectInfoModel {
  id?: string;
  organizationName: string;
  projectName: string;
  myRole: string;
  description: string;
  developerDetails: ProjectUserModel;
  managerDetails: ProjectUserModel;
  ctoDetails: ProjectUserModel;
}

export interface ProjectUserModel {
  id?: string;
  email: string;
  phone: string;
  firstName: string;
  lastName: string;
}
