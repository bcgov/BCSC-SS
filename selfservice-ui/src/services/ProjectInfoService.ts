import axios from '@/lib/axios';
import { ProjectInfoModel } from '@/models/ProjectInfoModel';
import { PROJECTINFO_URL } from '@/config/api-endpoints';
export class ProjectInfoService {
  public static async getProjectInfos() {
    return await axios.get(PROJECTINFO_URL);
  }
  public static async getProjectInfoById(id: string) {
    return await axios.get(PROJECTINFO_URL + '/' + id);
  }
  public static async createProjectInfo(projectinfoModel: ProjectInfoModel) {
    return await axios.post(PROJECTINFO_URL, projectinfoModel);
  }
  public static async updateProjectInfo(projectinfoModel: ProjectInfoModel) {
    return await axios.put(
      PROJECTINFO_URL + '/' + projectinfoModel.id,
      projectinfoModel
    );
  }

  /**
   * update project status
   * @param  {string} projectId
   * @param  {number} status
   */
  public static async updateStatusOfProject(projectId: string, status: number) {
    const data = {
      status,
      update: 'status'
    };
    return await axios.patch(`${PROJECTINFO_URL}/${projectId}`, data);
  }
}
