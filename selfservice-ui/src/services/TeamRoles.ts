import axios from '@/lib/axios';
// import { ProjectInfoModel } from '@/models/ProjectInfoModel';
import { TEAMROLE_URL } from '@/config/api-endpoints';
import { getUrl } from '@/lib/helpers';

export class TeamRoles {
  public static async getTeamRoles(projectId: number) {
    const teamURL = getUrl(TEAMROLE_URL, projectId);

    return await axios.get(teamURL);
  }
}
