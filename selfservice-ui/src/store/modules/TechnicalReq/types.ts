import { TechnicalReqModel } from '@/models/TechnicalReqModel';
export interface TechnicalReqState {
  loading?: boolean;
  successStatus?: boolean;
  errorStatus?: boolean;
  singleTechnicalReq: TechnicalReqModel;
  message: string;
}
