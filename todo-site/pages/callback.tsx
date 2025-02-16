"use client";
import { useEffect } from "react";
import { useRouter } from "next/router";
import { userManager } from "../lib/authConfig";

export default function Callback() {
  const router = useRouter();

  useEffect(() => {
    userManager
      .signinCallback()
      .then((user) => {
        if (user && user.access_token) {
          localStorage.setItem("token", user.access_token);
          router.push("/"); // Redirect to home after login
        } else {
          console.error("User or access_token is undefined", user);
          router.push("/login"); // Redirect to login if authentication failed
        }
      })
      .catch((err) => {
        console.error("Error during sign-in callback:", err);
        router.push("/login"); // Redirect on error
      });
  }, [router]);

  return <p>Processing login...</p>;
}
