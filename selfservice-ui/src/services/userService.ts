import axios from '@/lib/axios';
import { UserModel } from '@/models/UserModel';
import { USER_URL } from '@/config/api-endpoints';
export class UserService {
  /**
   * get user serive
   * @static
   * @returns promis
   */
  public static async getUsers(pageNumber: number = 1, records: number = 10) {
    return await axios.get(
      `${USER_URL}/?page=${pageNumber}&records=${records}`
    );
  }
  /**
   * get user
   * @static
   * @returns
   */
  public static async getUser() {
    return await axios.get(USER_URL);
  }
  /**
   * create user with token
   *
   * @static
   * @returns
   */
  public static async createUser(email: string, phone: string) {
    return await axios.post(USER_URL, {
      email,
      phone
    });
  }
  /**
   * update user with id
   * @static
   * @param {UserModel} userModel
   * @returns
   */
  public static async updateUser(userModel: UserModel) {
    return await axios.patch(USER_URL + '/' + userModel.id, userModel);
  }
  /**
   * remove user
   * @static
   * @param {string} id
   * @returns
   */
  public static async deleteUser(id: string) {
    return await axios.delete(USER_URL + '/' + id);
  }
}
