import axios from '@/lib/axios';
import { OIDCCONFIG_URL } from '@/config/api-endpoints';
import { getUrl } from '@/lib/helpers';

export default class ClientID {
  public static async getApiData(id: number) {
    const oidcURL = getUrl(OIDCCONFIG_URL, id);
    return await axios.get(oidcURL);
  }
}
