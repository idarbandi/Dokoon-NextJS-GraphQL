// withAuth.js
import React, { useEffect } from 'react';
import Router from 'next/router';
import { useMachine } from '@xstate/react';
import authMachine from './authMachine';

const withAuth = (WrappedComponent) => {
  return (props) => {
    const [state, send] = useMachine(authMachine);

    useEffect(() => {
      // Check if user is logged in
      fetch('http://localhost:8000/account/whoami/', {
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.username) {
            send({ type: 'LOGIN' });
            Router.push('/dashboard'); // Redirect to dashboard if logged in
          } else {
            send({ type: 'LOGOUT' });
          }
        })
        .catch((err) => {
          console.error('Verification failed', err);
          send({ type: 'LOGOUT' });
        });
    }, [send]);

    if (state.matches('loggedOut')) {
      return null; // Or you can render a loading spinner
    }

    return <WrappedComponent {...props} />;
  };
};

export default withAuth;
