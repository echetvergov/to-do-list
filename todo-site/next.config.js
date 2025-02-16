/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  images: {
    domains: [], // If using external images, add domains here
  },
};

module.exports = nextConfig;
