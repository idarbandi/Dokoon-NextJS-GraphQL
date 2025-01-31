import { createContext, useContext, useState } from 'react';
import { LoginMutation } from '../graphQL/graphQL';
import { ApolloClient, HttpLink, InMemoryCache } from '@apollo/client';
import Router from 'next/router';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const auth = useAuthProvider();
  return <AuthContext.Provider value={auth}>{children}</AuthContext.Provider>;
}

export const useAuthentication = () => {
  return useContext(AuthContext);
};

function useAuthProvider() {
  const [authToken, setAuthToken] = useState(null);
  const [userName, setUserName] = useState(null);
  const [error, setError] = useState(null);

  // Create a "dirty" Apollo client for testing
  // In authorization.js - Fix the Apollo Client setup
  const createApolloClient = () => {
    const httpLink = new HttpLink({
      uri: 'http://127.0.0.1:8000/graphQl/', // ← Fix IP and remove trailing slash
      credentials: 'include',
    });

    return new ApolloClient({
      link: httpLink,
      cache: new InMemoryCache(),
      defaultOptions: {
        watchQuery: {
          fetchPolicy: 'no-cache',
          errorPolicy: 'ignore',
        },
        query: {
          fetchPolicy: 'no-cache',
          errorPolicy: 'all',
        },
        mutate: {
          fetchPolicy: 'no-cache',
          errorPolicy: 'all',
        },
      },
    });
  };

  // Modify the signIn function to log detailed errors
  const signIn = async ({ username, password }) => {
    try {
      const client = createApolloClient();
      const { data, errors } = await client.mutate({
        mutation: LoginMutation,
        variables: { username, password },
      });

      console.log('Full response:', { data, errors }); // Add this

      if (errors) {
        throw new Error(errors[0].message);
      }

      if (data?.tokenAuth?.token) {
        setAuthToken(data.tokenAuth.token);
        setUserName(data.tokenAuth.payload.username);
        localStorage.setItem('DokoonAuthToken', JSON.stringify(data.tokenAuth.token));
        console.log('TOKEN SET', data);
        Router.push('/dashboard');
      }
    } catch (err) {
      console.error('Full error details:', err);
      setError(err.message || 'Authentication failed');
      throw err; // Re-throw for error boundaries
    }
  };

  return {
    authToken,
    signIn,
    error,
  };
}
