import axios from '@/lib/axios';
import { ProjectInfoModel } from '@/models/ProjectInfoModel';
import { PROJECTINFO_URL, PROJECTHISTORY_URL } from '@/config/api-endpoints';
import { getUrl } from '@/lib/helpers';
export class ProjectInfoService {
  /**
   * get list of project
   */
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
      update: 'status',
    };
    return await axios.patch(`${PROJECTINFO_URL}/${projectId}`, data);
  }
  /**
   * delete project
   * @param  {string} projectId
   */
  public static async deleteProject(projectId: string) {
    return await axios.delete(`${PROJECTINFO_URL}/${projectId}`);
  }
  public static async getProjectHistory(id: string) {
    const historyUrl = getUrl(PROJECTHISTORY_URL, id);
    return await axios.get(historyUrl);
  }
}
