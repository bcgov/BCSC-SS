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
  dev = 2,
  devComplete = 3,
  complianceChecks = 4,
  complianceReview = 5,
  complianceChecksComplete = 6,
  awaitingProdKeys = 7,
  inProd = 8,
}

export { projectRoles, algorithmBase, projectStatus };
