enum projectRoles {
  // This Enum provides the list of Project Roles.
  developer = 1,
  manager = 2,
  cto = 3,
}
enum algorithmBase {
  // This Enum provides the list of algorithams.
  SignedJWT = 1,
  SecureJWT = 2,
}

enum projectStatus {
  draft = 1,
  development = 2,
  developmentComplete = 3,
  complianceChecks = 4,
  awaitingApproval = 5,
  awaitingStagingKeys = 6,
  awaitingProductionUse = 7,
  readyForFirstCitizenUse = 8,
}

export { projectRoles, algorithmBase, projectStatus };
