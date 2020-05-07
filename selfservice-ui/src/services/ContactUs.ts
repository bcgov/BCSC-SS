import axios from '@/lib/axios';
import { ContactDetailsModel } from '@/models/ContactDetailsModel';
import { CONTACTUS_URL } from '@/config/api-endpoints';
export class ContactUs {
  public static async addContactUs(contactDetails: ContactDetailsModel) {
    return await axios.post(CONTACTUS_URL, contactDetails);
  }
}
