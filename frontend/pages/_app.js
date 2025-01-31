import '@/styles/globals.css';
import { AuthProvider } from './api/authorization';

export default function App({ Component, pageProps }) {
  return (
    <AuthProvider>
      <Component {...pageProps} />
    </AuthProvider>
  );
}
