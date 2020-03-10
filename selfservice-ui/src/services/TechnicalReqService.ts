import axios from '@/lib/axios';
import { TechnicalReqModel } from '@/models/TechnicalReqModel';
import { TECHNICALREQ_URL } from '@/config/api-endpoints';
import { getUrl } from '@/lib/helpers';
export class TechnicalReqService {
  public static async getTechnicalReqs() {
    return await axios.get(TECHNICALREQ_URL);
  }
  public static async getTechnicalReqByProjectId(id: string) {
    const techUrl = getUrl(TECHNICALREQ_URL, id);
    return await axios.get(techUrl);
  }
  public static async createTechnicalReq(technicalreqModel: any) {
    const techUrl = getUrl(TECHNICALREQ_URL, technicalreqModel.projectId);

    return await axios.post(techUrl, technicalreqModel);
  }
  public static async updateTechnicalReq(technicalreqModel: TechnicalReqModel) {
    const techUrl = getUrl(TECHNICALREQ_URL, technicalreqModel.projectId);
    return await axios.put(techUrl, technicalreqModel);
  }
}
