"use client";
import { signOutRedirect } from "../lib/authConfig";

export default function Logout() {
  return <button onClick={signOutRedirect}>Log Out</button>;
}
