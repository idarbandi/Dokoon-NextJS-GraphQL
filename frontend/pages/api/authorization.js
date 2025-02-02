import { createContext, useContext, useState } from 'react';
import client from '../graphQL/graphQL';
import Router from 'next/router';
import { LoginMutation } from '../graphQL/graphQL';

/**
 * ********************************************************************************
 * 🌐 Dokoon-NextJS-GraphQL
 * 👤 Author: idarbandi
 * 📁 GitHub: https://github.com/idarbandi/Dokoon-NextJS-GraphQL
 * ✉️ Email: darbandidr99@gmail.com
 * 💼 LinkedIn: https://www.linkedin.com/in/amir-darbandi-72526b25b/
 * 🖥 Framework: NextJS
 *
 * This project was developed by idarbandi.
 * We hope you find it useful! Contributions and feedback are welcome.
 * ********************************************************************************
 */

const DokoonAuthContext = createContext();

// کامپوننت ارائه‌دهنده احراز هویت
export function DokoonAuthProvider({ children }) {
  const auth = dokoon_useAuthProvider();
  return <DokoonAuthContext.Provider value={auth}>{children}</DokoonAuthContext.Provider>;
}

// هوک برای استفاده از احراز هویت
export const useDokoonAuthentication = () => {
  return useContext(DokoonAuthContext);
};

// هوک برای مدیریت احراز هویت
function dokoon_useAuthProvider() {
  const [error, setError] = useState(null);

  const dokoon_signIn = async ({ username, password }) => {
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
    dokoon_signIn,
    error,
  };
}
