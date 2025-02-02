// withAuth.js

// این فایل یک HOC (Higher-Order Component) تعریف می‌کند تا تنها به کاربران احراز هویت‌شده اجازه دسترسی بدهد

import React, { useEffect } from 'react';
import Router from 'next/router';
import { useQuery } from '@apollo/client';
import { dokoonUserDetails } from './graphQL/graphQL'; // کوئری برای دریافت جزئیات کاربر

const withAuth = (WrappedComponent) => {
  return (props) => {
    // انجام کوئری برای دریافت جزئیات کاربر
    const { data, loading, error } = useQuery(dokoonUserDetails, {
      fetchPolicy: 'network-only',
      ssr: false,
    });

    useEffect(() => {
      if (!loading) {
        // اگر خطا وجود داشته باشد یا کاربر احراز هویت نشده باشد، به صفحه ورود هدایت شود
        if (error || !data?.userDetails) {
          Router.push('/Signin');
        }
      }
    }, [data, loading, error]);

    if (loading) {
      return <p>در حال بارگذاری...</p>; // نمایش پیام بارگذاری در حین انجام کوئری
    }

    if (error || !data?.userDetails) {
      return null; // بازگشت به صفحه ورود در صورت وجود خطا یا عدم احراز هویت
    }

    return <WrappedComponent {...props} />; // نمایش کامپوننت هدف در صورت احراز هویت
  };
};

export default withAuth;
