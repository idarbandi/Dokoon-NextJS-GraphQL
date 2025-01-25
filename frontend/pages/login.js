import React, { useState, useEffect, forwardRef } from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import { useRouter } from 'next/router';
import Router from 'next/router';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import LockOpenOutlined, { LocalActivityOutlined } from '@material-ui/icons';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Box from '@mui/material/Box';
import Alert from '@mui/material/Alert';
import { useMachine } from '@xstate/react';
import authMachine from './authMachine';
import { makeStyles } from '@material-ui/core';

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  errorContainer: { marginTop: 20, marginBottom: 20 },
  errorAlert: { backgroundColor: '#f44336' },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '100%',
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

const Login = forwardRef((props, ref) => {
  const classes = useStyles();
  const [csrfToken, setCsrfToken] = useState('');
  const [userName, setUserName] = useState('');
  const [error, setError] = useState('');
  const [password, setPassword] = useState('');
  const [state, send] = useMachine(authMachine);
  const router = useRouter();

  useEffect(() => {
    // Fetch CSRF token
    fetch('http://localhost:8000/account/csrf/', {
      credentials: 'include',
    })
      .then((res) => res.json())
      .then((data) => {
        const csrfToken = data.csrfToken;
        setCsrfToken(csrfToken);
        console.log('CSRF Token:', csrfToken);
        console.log('CSRF Token Length:', csrfToken.length);
      })
      .catch((err) => {
        setError(err.message);
      });
  }, []);

  useEffect(() => {
    // Check if user is already logged in
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
          router.push('/dashboard'); // Redirect to dashboard if already logged in
        }
      })
      .catch((err) => {
        console.error('Verification failed', err);
      });
  }, [router, send]);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Submitting with CSRF Token:', csrfToken);

    // Additional logging to verify headers and token
    console.log('Headers:', {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken,
    });

    fetch('http://localhost:8000/account/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
      },
      credentials: 'include',
      body: JSON.stringify({ username: userName, password: password }),
    })
      .then((response) => {
        if (response.ok) {
          console.log('Login successful');
          send({ type: 'LOGIN' });
          router.push('/dashboard');
        } else {
          setError('Could Not Connect To The Server Correctly');
        }
      })
      .catch((err) => {
        setError(err.message);
      });
  };

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Box className={classes.errorContainer}>
          {error && (
            <Alert severity="error" className={classes.errorAlert}>
              {error}
            </Alert>
          )}
        </Box>
        <Avatar className={classes.avatar}>
          <LocalActivityOutlined />
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign In
        </Typography>
        <form className={classes.form} onSubmit={handleSubmit} noValidate ref={ref}>
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="username"
            label="Username"
            name="username"
            autoComplete="username"
            autoFocus
            onChange={(e) => setUserName(e.target.value)}
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="current-password"
            onChange={(e) => setPassword(e.target.value)}
          />
          <FormControlLabel control={<Checkbox value="remember" color="primary" />} label="Remember me" />
          <Button type="submit" fullWidth variant="contained" color="primary" className={classes.submit}>
            Sign In
          </Button>
          <Grid container>
            <Grid item xs>
              <Link href="#" variant="body2">
                Forgot Password
              </Link>
            </Grid>
            <Grid item>
              <Link href="#" variant="body2">
                Don't Have an Account? Sign Up
              </Link>
            </Grid>
          </Grid>
        </form>
      </div>
    </Container>
  );
});

export default Login;
