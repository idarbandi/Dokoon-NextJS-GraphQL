import React, { useState } from 'react';

export const login = () => {
  const [csrfToken, setCsrfToken] = useState('');

  React.useEffect(() => {
    fetch('http://127.0.0.1:8000/account/csrf/')
      .then((res) => {
        let csrfToken = res.headers.get('X-CSRFToken');
        setCsrfToken(csrfToken);
      })
      .catch((err) => {
        alert(err);
      });
  }, []);

  return <>login</>;
};

export default login;
