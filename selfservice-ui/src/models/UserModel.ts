export interface UserModel {
  id: string;
  referenceId: string;
  firstName: string;
  lastName: string;
  email: string;
  role: string;
  createdDate: string;
}
export interface UserListModel {
  count: number;
  users: UserModel[];
}
