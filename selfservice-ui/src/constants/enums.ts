enum projectRoles {
  // This Enum provides the list of Project Roles.
  developer = 1,
  manager = 2,
  cto = 3
}
enum algorithamBase {
  // This Enum provides the list of algorithams.
  SignedJWT = 1,
  SecureJWT = 2
}

const projectRolesList = {
  // const array for project role name cxonvertion
  1: 'developer',
  2: 'manager',
  3: 'cto'
};

export { projectRoles, algorithamBase, projectRolesList };
