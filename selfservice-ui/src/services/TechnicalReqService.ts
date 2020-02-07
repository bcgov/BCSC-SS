import axios from '@/lib/axios';
import { TechnicalReqModel } from '@/models/TechnicalReqModel';
import { TECHNICALREQ_URL } from '@/config/api-endpoints';
export class TechnicalReqService {
  public static async getTechnicalReqs() {
    return await axios.get(TECHNICALREQ_URL);
  }
  public static async getTechnicalReqByProjectId(id: string) {
    const techUrl = this.getUrl(id);
    return await axios.get(techUrl);
  }
  public static async createTechnicalReq(technicalreqModel: any) {
    const techUrl = this.getUrl(technicalreqModel.projectId);

    return await axios.post(techUrl, technicalreqModel);
  }
  public static async updateTechnicalReq(technicalreqModel: TechnicalReqModel) {
    return await axios.put(
      TECHNICALREQ_URL + '/' + technicalreqModel.id,
      technicalreqModel
    );
  }
  // public static async deleteTechnicalReq(id: string) {
  //   return await axios.delete(TECHNICALREQ_URL + '/' + id);
  // }

  public static getUrl(projectId: any) {
    return TECHNICALREQ_URL.replace('<projectId>', projectId);
  }
}
