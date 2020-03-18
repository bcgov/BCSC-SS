import axios from '@/lib/axios';
// import { ProjectInfoModel } from '@/models/ProjectInfoModel';
import { TESTACCOUNT_URL } from '@/config/api-endpoints';
export class TestAccounts {
  public static async addTestAccounts(testAccountData: any) {
    return await axios.post(TESTACCOUNT_URL, testAccountData);
  }
}
