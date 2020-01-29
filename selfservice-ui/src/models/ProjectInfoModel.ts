export interface ProjectInfoModel {
  id?: string;
  organizationName: string;
  projectName: string;
  myRole: number;
  description: string;
  users: ProjectUserModel[];
}

export interface ProjectUserModel {
  id?: string;
  email: string;
  phone: string;
  firstName: string;
  lastName: string;
  role: number;
}
