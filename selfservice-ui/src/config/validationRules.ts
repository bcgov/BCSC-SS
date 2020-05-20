const rules = {
  length: (len: any) => (v: any) =>
    (v || '').length >= len || 'Invalid character length, required ' + len,
  maxLength: (len: any) => (v: any) =>
    (v || '').length <= len || 'Invalid character length, max length ' + len,
  required: (v: any) => !!v || 'This field is required',
  email: (v: any) =>
    /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/.test(v) ||
    'E-mail must be valid',
  url: (v: any) => {
    if (v === '') {
      return true;
    } else {
      return (
        /^(?:http(s)?:\/\/)[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$/.test(
          v
        ) || ' must be valid URL'
      );
    }
  },
  urlLocalHost: (v: any) => {
    if (v === '') {
      return true;
    } else {
      return (
        // tslint:disable
        /^((?:http(s)?:\/\/)[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+|((?:http(s)?:\/\/)localhost).*)$/.test(
          v
        ) || ' must be valid URL (http://localhost allowed)'
      );
      // tslint:enable
    }
  },
};

export default rules;
