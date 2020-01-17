import { TechnicalReqModel } from '@/models/TechnicalReqModel';
export interface TechnicalReqState {
  technicalreqList: TechnicalReqModel[];
  loading?: boolean;
  successStatus?: boolean;
  errorStatus?: boolean;
  singleTechnicalReq: TechnicalReqModel[];
  message: string;
}
