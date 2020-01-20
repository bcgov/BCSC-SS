import axios from '@/lib/axios';
import { TechnicalReqModel } from '@/models/TechnicalReqModel';
import { TECHNICALREQ_URL } from '@/config/api-endpoints';
export class TechnicalReqService {
  public static async getTechnicalReqs() {
    return await axios.get(TECHNICALREQ_URL);
  }
  public static async getTechnicalReqById(id: string) {
    return await axios.get(TECHNICALREQ_URL + '/' + id);
  }
  public static async createTechnicalReq(technicalreqModel: any) {
    return await axios.post(TECHNICALREQ_URL, technicalreqModel);
  }
  public static async updateTechnicalReq(technicalreqModel: TechnicalReqModel) {
    return await axios.put(
      TECHNICALREQ_URL + '/' + technicalreqModel.id,
      technicalreqModel
    );
  }
  public static async deleteTechnicalReq(id: string) {
    return await axios.delete(TECHNICALREQ_URL + '/' + id);
  }
}
