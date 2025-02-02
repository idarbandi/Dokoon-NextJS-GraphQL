// withAuth.js
import React, { useEffect } from 'react';
import Router from 'next/router';
import { useMachine } from '@xstate/react';
import { useQuery } from '@apollo/client';
import authMachine from './authMachine';
import { userDetails } from './graphQL/graphQL'; // Import the userDetails query

const withAuth = (WrappedComponent) => {
  return (props) => {
    const [state, send] = useMachine(authMachine);
    const { data, loading, error } = useQuery(userDetails); // Execute the userDetails query

    useEffect(() => {
      if (loading) return; // If the query is still loading, do nothing

      if (error || !data?.userDetails?.username) {
        send({ type: 'LOGOUT' });
        Router.push('/login'); // Redirect to login if not authenticated
      } else {
        send({ type: 'LOGIN' });
      }
    }, [data, loading, error, send]);

    if (state.matches('loggedOut')) {
      return null; // Or you can render a loading spinner
    }

    return <WrappedComponent {...props} />;
  };
};

export default withAuth;
