import axios from '@/lib/axios';
// import { PackageModel } from '@/models/PackageModel';
import { PACKAGE_URL, TECHNICALREQ_URL } from '@/config/api-endpoints';
export class PackageService {
  public static async getPackages() {
    return await axios.get(PACKAGE_URL + '/');
  }

  public static async updatePackageProject(
    projectId: number,
    slectedPackage: number
  ) {
    return await axios.patch(TECHNICALREQ_URL, {
      scopePackageId: slectedPackage,
      update: 'package'
    });
  }
}
