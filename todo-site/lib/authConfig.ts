import { UserManager } from "oidc-client-ts";

const cognitoAuthConfig = {
  authority: "https://eu-central-1audrmyxlq.auth.eu-central-1.amazoncognito.com",
  client_id: "rpioob2seiam1trj4pl25kmba",
  redirect_uri: "https://day8lfrmokkaq.cloudfront.net",
  response_type: "code",
  scope: "openid email profile",
};

// Initialize the UserManager
export const userManager = new UserManager(cognitoAuthConfig);

// Logout function
export async function signOutRedirect() {
  const logoutUri = "https://day8lfrmokkaq.cloudfront.net/";
  window.location.href = `${cognitoAuthConfig.authority}/logout?client_id=${cognitoAuthConfig.client_id}&logout_uri=${encodeURIComponent(logoutUri)}`;
}
