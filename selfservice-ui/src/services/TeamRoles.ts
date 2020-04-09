import axios from '@/lib/axios';
// import { ProjectInfoModel } from '@/models/ProjectInfoModel';
import { TEAMROLE_URL } from '@/config/api-endpoints';
import { getUrl } from '@/lib/helpers';

export class TeamRoles {
  public static async getTeamRoles(projectId: number) {
    const teamURL = getUrl(TEAMROLE_URL, projectId);

    return await axios.get(teamURL);
  }
  public static async addTeamMember(userDetails: any, projectId: number) {
    const teamURL = getUrl(TEAMROLE_URL, projectId);

    return await axios.post(teamURL, userDetails);
  }
  public static async getTeamMember(projectId: number, memberId: number) {
    const teamURL = getUrl(TEAMROLE_URL, projectId);

    return await axios.get(`${teamURL}/${memberId}`);
  }
  public static async updateTeamMember(
    userDetails: any,
    projectId: number,
    memberId: number
  ) {
    const teamURL = getUrl(TEAMROLE_URL, projectId);

    return await axios.put(`${teamURL}/${memberId}`, userDetails);
  }
  public static async deleteTeamMember(projectId: number, memberId: number) {
    const teamURL = getUrl(TEAMROLE_URL, projectId);
    return await axios.delete(`${teamURL}/${memberId}`);
  }
}
