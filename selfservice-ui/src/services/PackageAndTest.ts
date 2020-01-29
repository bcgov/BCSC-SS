import axios from '@/lib/axios';
import { PACKAGE_URL, TECHNICALREQ_URL } from '@/config/api-endpoints';
export class PackageAndTest {
  public static async getPackages() {
    return await axios.get(PACKAGE_URL);
  }

  public static async updatePackageProject(
    projectId: string,
    slectedPackage: number
  ) {
    return await this.updatePackageOrTestToProject(projectId, {
      scopePackageId: slectedPackage,
      update: 'package'
    });
  }

  public static async updatePackageOrTestToProject(
    projectId: string,
    data: any
  ) {
    const techUrl = TECHNICALREQ_URL.replace('<projectId>', projectId);
    return await axios.patch(techUrl, data);
  }

  public static async updateTestRequestProject(
    projectId: string,
    noOfTestAccount: number,
    noteTestAccount: string
  ) {
    return await this.updatePackageOrTestToProject(projectId, {
      noOfTestAccount,
      noteTestAccount,
      update: 'test-account'
    });
  }
}
