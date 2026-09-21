# FinTrack AI

A lightweight, mobile-first asset management application built with React Native and Expo. FinTrack AI is designed for real-time tracking of multi-currency portfolios, specifically optimized for high-volatility markets where manual exchange rate adjustments are essential.

## Key Features
- **Multi-Currency Support**: Track assets across USD, EUR, GBP, JPY, CNY, and IRT.
- **Manual Rate Override**: Customizable exchange rate inputs to adapt to real-time market volatility.
- **Smart Categorization**: Native support for Crypto, Gold, Cash, Stocks, and Other assets.
- **Optimized Performance**: Built with `useMemo` for efficient Net Worth calculations and smooth UI responsiveness.
- **Local Persistence**: Secure data storage using AsyncStorage.

## Tech Stack
- **Frontend**: React Native, Expo
- **State Management**: React Hooks (useState, useMemo)
- **Persistence**: AsyncStorage
- **Deployment**: EAS (Expo Application Services)

## Installation
1. Clone the repository:
   `git clone <your-repository-url>`
2. Install dependencies:
   `npm install`
3. Start the development server:
   `npx expo start`

## License
MIT
