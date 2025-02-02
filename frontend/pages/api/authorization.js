// authorization.js
import { createContext, useContext, useState } from 'react';
import client from '../graphQL/graphQL';
import Router from 'next/router';
import { LoginMutation } from '../graphQL/graphQL';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const auth = useAuthProvider();
  return <AuthContext.Provider value={auth}>{children}</AuthContext.Provider>;
}

export const useAuthentication = () => {
  return useContext(AuthContext);
};

function useAuthProvider() {
  const [error, setError] = useState(null);

  const signIn = async ({ username, password }) => {
    try {
      const { data, errors } = await client.mutate({
        mutation: LoginMutation,
        variables: { username, password },
      });

      console.log('Full response:', { data, errors });

      if (errors) {
        throw new Error(errors[0].message);
      }

      if (data?.tokenAuth?.token) {
        console.log('Login successful');
        Router.push('/dashboard');
      } else {
        setError('Authentication failed');
      }
    } catch (err) {
      console.error('Full error details:', err);
      setError(err.message || 'Authentication failed');
      throw err;
    }
  };

  return {
    signIn,
    error,
  };
}
