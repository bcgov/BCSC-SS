import axios from '@/lib/axios';
import {
  PACKAGE_URL,
  TECHNICALREQ_URL,
  PROJECTINFO_URL
} from '@/config/api-endpoints';
export default class ClientID {
  public static async getApiData() {
    // return await axios.get(PACKAGE_URL);
    const apiData = {
      data: {
        clientId: 'abcd',
        clientSecret: 'test',
        testUserAccounts: [
          {
            userName: 'test user',
            idKey: 'test id key'
          },
          {
            userName: 'test user',
            idKey: 'test id key'
          }
        ]
      }
    };
    return apiData;
  }
}
