import { PackageModel } from '@/models/PackageModel';
export interface PackageState {
  packageList: PackageModel[];
  loading?: boolean;
  successStatus?: boolean;
  errorStatus?: boolean;
  message: string;
}
