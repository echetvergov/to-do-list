"use client";
import { userManager } from "../lib/authConfig";

export default function Login() {
  const handleLogin = async () => {
    await userManager.signinRedirect();
  };

  return <button onClick={handleLogin}>Sign In</button>;
}
