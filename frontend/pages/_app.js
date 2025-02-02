// _app.js
import { ApolloProvider } from '@apollo/client';
import client from './graphQL/graphQL';
import { AuthProvider } from './api/authorization';
import '../styles/globals.css';

function MyApp({ Component, pageProps }) {
  return (
    <ApolloProvider client={client}>
      <AuthProvider>
        <Component {...pageProps} />
      </AuthProvider>
    </ApolloProvider>
  );
}

export default MyApp;
