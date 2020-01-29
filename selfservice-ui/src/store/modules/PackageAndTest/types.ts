import { PackageAndTest } from '@/models/PackageAndTest';
export interface PackageState {
  packageList: PackageAndTest[];
  loading?: boolean;
  successStatus?: boolean;
  errorStatus?: boolean;
  message: string;
}
