import React, { useState, useEffect, forwardRef } from 'react';

import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import LockOpenOutlined, { LocalActivityOutlined } from '@material-ui/icons';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { makeStyles } from '@material-ui/core';
import Box from '@mui/material/Box';
import Alert from '@mui/material/Alert';

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
    width: '100%', // Fix IE 11 issue.
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

  useEffect(() => {
    fetch('http://localhost:8000/account/csrf/', {
      credentials: 'include',
    })
      .then((res) => {
        let csrfToken = res.headers.get('X-CSRFToken');
        setCsrfToken(csrfToken);
      })
      .catch((err) => {
        setError(err);
      });
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
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
          console.log(response);
        } else {
          setError('Could Not Connect To The Server Correctly');
        }
      })
      .catch((err) => {
        setError(err);
      });
  };

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Box className={classes.errorContainer}>
          {' '}
          {error && (
            <Alert severity="error" className={classes.errorAlert}>
              {' '}
              {error}{' '}
            </Alert>
          )}{' '}
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
