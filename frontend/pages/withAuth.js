// withAuth.js
import React, { useEffect } from 'react';
import Router from 'next/router';
import { useQuery } from '@apollo/client';
import { userDetails } from './graphQL/graphQL';

const withAuth = (WrappedComponent) => {
  return (props) => {
    const { data, loading, error } = useQuery(userDetails, {
      fetchPolicy: 'network-only',
      ssr: false,
    });

    useEffect(() => {
      if (!loading) {
        if (error || !data?.userDetails) {
          Router.push('/Signin');
        }
      }
    }, [data, loading, error]);

    if (loading) {
      return <p>Loading...</p>;
    }

    if (error || !data?.userDetails) {
      return null;
    }

    return <WrappedComponent {...props} />;
  };
};

export default withAuth;
