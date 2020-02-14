import axios from '@/lib/axios';
import { OIDCCONFIG_URL } from '@/config/api-endpoints';
import { getUrl } from '@/lib/helpers';

export default class ClientID {
  public static async getApiData(id: number) {
    // return await axios.get(PACKAGE_URL);
    const oidcURL = getUrl(OIDCCONFIG_URL, id);
    return await axios.get(oidcURL);
    // const apiData = {
    //   data: {
    //     clientId: 'abcd',
    //     clientSecret: 'test',
    //     testUserAccounts: [
    //       {
    //         userName: 'test user',
    //         idKey: 'test id key'
    //       },
    //       {
    //         userName: 'test user',
    //         idKey: 'test id key'
    //       }
    //     ]
    //   }
    // };
    // return apiData;
  }
}
