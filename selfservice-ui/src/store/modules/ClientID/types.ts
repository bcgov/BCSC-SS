import { PackageAndTest } from '@/models/PackageAndTest';
export interface ClientIdState {
  apiData: any; // PackageAndTest[];
  loading?: boolean;
  successStatus?: boolean;
  errorStatus?: boolean;
  message: string;
}
