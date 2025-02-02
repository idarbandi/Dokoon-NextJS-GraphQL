// dashboard.js
import React from 'react';
import withAuth from './withAuth';
import DashboardContent from './DashboardContent';

const DashboardPage = () => {
  return <DashboardContent />;
};

export default withAuth(DashboardPage);
