import React from 'react';
import withAuth from './withAuth';
import DashboardContent from './DashboardContent'; // Import DashboardContent

const DashboardPage = () => {
  return <DashboardContent />;
};

export default withAuth(DashboardPage);
