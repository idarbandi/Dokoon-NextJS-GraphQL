// DashboardContent.js
import React, { useState, useEffect } from 'react';
import { styled, createTheme, ThemeProvider } from '@mui/material/styles';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Router from 'next/router';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import PowerSettingsNewIcon from '@mui/icons-material/PowerSettingsNew';
import { useMachine } from '@xstate/react';
import authMachine from './authMachine';
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import Drawer from '@mui/material/Drawer';
import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import DashboardIcon from '@mui/icons-material/Dashboard';
import BarChartIcon from '@mui/icons-material/BarChart';
import SettingsIcon from '@mui/icons-material/Settings';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Chart from './charts';
import Deposits from './deposits';
import Orders from './orders';
import Avatar from '@mui/material/Avatar';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';

const drawerWidth = 240;

const AppBarStyled = styled(AppBar, {
  shouldForwardProp: (prop) => prop !== 'open',
})(({ theme, open }) => ({
  zIndex: theme.zIndex.drawer + 1,
  transition: theme.transitions.create(['width', 'margin'], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  ...(open && {
    marginLeft: drawerWidth,
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  }),
}));

const DrawerStyled = styled(Drawer, { shouldForwardProp: (prop) => prop !== 'open' })(({ theme, open }) => ({
  '& .MuiDrawer-paper': {
    position: 'relative',
    whiteSpace: 'nowrap',
    width: drawerWidth,
    transition: theme.transitions.create('width', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
    boxSizing: 'border-box',
    ...(!open && {
      overflowX: 'hidden',
      transition: theme.transitions.create('width', {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.leavingScreen,
      }),
      width: theme.spacing(7),
      [theme.breakpoints.up('sm')]: {
        width: theme.spacing(9),
      },
    }),
  },
}));

const Main = styled('main')(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'light' ? theme.palette.grey[100] : theme.palette.grey[900],
  flexGrow: 1,
  height: '100vh',
  overflow: 'auto',
}));

const mdTheme = createTheme();

const DashboardContent = () => {
  const [open, setOpen] = useState(true);
  const [anchorEl, setAnchorEl] = useState(null);
  const [state, send] = useMachine(authMachine);
  const [error, setError] = useState('');

  const openMenu = Boolean(anchorEl);

  // Toggle the drawer open/close state
  const toggleDrawer = () => {
    setOpen(!open);
  };

  // Handle user menu actions
  const handleMenuClick = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleCloseMenu = () => {
    setAnchorEl(null);
  };

  // Fetch current user data using GraphQL
  const { loading: userLoading, error: userError, data: userData } = useQuery(GET_CURRENT_USER);

  // Logout mutation
  const [logout, { loading: logoutLoading }] = useMutation(LOGOUT_MUTATION, {
    onCompleted: (data) => {
      if (data.logout.success) {
        send({ type: 'LOGOUT' });
        Router.push('/login');
      } else {
        setError('Logout failed');
      }
    },
    onError: (error) => {
      console.error('Logout error:', error);
      setError(error.message);
    },
  });

  const handleLogout = () => {
    logout();
  };

  // Render loading state or error
  if (userLoading) return <p>Loading...</p>;
  if (userError) return <p>Error: {userError.message}</p>;

  const user = userData?.me;
  const username = user?.username || 'Guest';
  const avatarUrl = user?.avatarUrl || 'avatar1.jpg'; // Default avatar if none

  return (
    <ThemeProvider theme={mdTheme}>
      <Box sx={{ display: 'flex' }}>
        <AppBarStyled position="absolute" open={open}>
          <Toolbar sx={{ pr: '24px' }}>
            <IconButton
              edge="start"
              color="inherit"
              aria-label="open drawer"
              onClick={toggleDrawer}
              sx={{
                marginRight: '36px',
                ...(open && { display: 'none' }),
              }}
            >
              <MenuIcon />
            </IconButton>
            <Typography component="h1" variant="h6" color="inherit" noWrap sx={{ flexGrow: 1 }}>
              داشبورد
            </Typography>

            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
              <Typography variant="body1">{username}</Typography>
              <IconButton onClick={handleMenuClick}>
                <Avatar alt={username} src={avatarUrl} />
              </IconButton>
              <Menu
                id="basic-menu"
                anchorEl={anchorEl}
                open={openMenu}
                onClose={handleCloseMenu}
                MenuListProps={{
                  'aria-labelledby': 'basic-button',
                }}
              >
                <MenuItem onClick={handleCloseMenu}>پروفایل</MenuItem>
                <MenuItem onClick={handleLogout} disabled={logoutLoading}>
                  خروج
                  <PowerSettingsNewIcon sx={{ ml: 1 }} />
                </MenuItem>
              </Menu>
            </Box>
          </Toolbar>
        </AppBarStyled>
        <DrawerStyled variant="permanent" open={open}>
          <Toolbar
            sx={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'flex-end',
              px: [1],
            }}
          >
            <IconButton onClick={toggleDrawer}>
              <ChevronLeftIcon />
            </IconButton>
          </Toolbar>
          <List>
            <ListItemButton>
              <ListItemIcon>
                <DashboardIcon />
              </ListItemIcon>
              <ListItemText primary="داشبورد" />
            </ListItemButton>
            <ListItemButton>
              <ListItemIcon>
                <BarChartIcon />
              </ListItemIcon>
              <ListItemText primary="گزارشات" />
            </ListItemButton>
            <ListItemButton>
              <ListItemIcon>
                <SettingsIcon />
              </ListItemIcon>
              <ListItemText primary="تنظیمات" />
            </ListItemButton>
          </List>
        </DrawerStyled>
        <Main sx={{ pt: 4, pb: 4 }}>
          <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
            <Grid container spacing={3}>
              <Grid item xs={12} md={8} lg={9}>
                <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
                  <Chart />
                </Paper>
              </Grid>
              <Grid item xs={12} md={4} lg={3}>
                <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
                  <Deposits />
                </Paper>
              </Grid>
              <Grid item xs={12}>
                <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
                  <Orders />
                </Paper>
              </Grid>
            </Grid>
          </Container>
        </Main>
      </Box>
    </ThemeProvider>
  );
};

export default DashboardContent;
