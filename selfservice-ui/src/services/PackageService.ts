import axios from '@/lib/axios';
// import { PackageModel } from '@/models/PackageModel';
import { PACKAGE_URL, TECHNICALREQ_URL } from '@/config/api-endpoints';
export class PackageService {
  public static async getPackages() {
    return await axios.get(PACKAGE_URL);
  }

  public static async updatePackageProject(
    projectId: string,
    slectedPackage: number
  ) {
    const techUrl = TECHNICALREQ_URL.replace('<projectId>', projectId);
    return await axios.patch(techUrl, {
      scopePackageId: slectedPackage,
      update: 'package'
    });
  }
}
