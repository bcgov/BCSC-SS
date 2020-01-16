const rules = {
  length: (len: any) => (v: any) =>
    (v || '').length >= len || 'Invalid character length, required ' + len,
  required: (v: any) => !!v || 'This field is required',
  email: (v: any) =>
    /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) ||
    'E-mail must be valid'
};

export default rules;
