/** ********************************************************************************
 * Dokoon Project
 * Author: Idarbandi
 * GitHub: https://github.com/idarbandi/Dokoon-NextDRF
 * Email: darbandidr99@gmail.com
 *
 * This project was developed by Idarbandi.
 * We hope you find it useful! Contributions and feedback are welcome.
 * ****************************************************************************** */

import React, { useRef, useEffect, forwardRef } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Container from '@material-ui/core/Container';
import List from '@material-ui/core/List';
import Link from 'next/link';

// استایل‌های کامپوننت هدر
const useDokoonStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  appbarDesktop: {
    backgroundColor: '#f8f8f8',
    color: '#fff',
  },
  appbarMain: {
    backgroundColor: '#2d2d2d',
  },
  appbarSecondary: {
    backgroundColor: '#525050',
    color: '#fff',
  },
  appbarPromotion: {
    backgroundColor: '#2d2d2d',
    color: '#fff',
    margin: theme.spacing(0, 0, 8),
    ['@media (max-width:600px)']: {
      margin: theme.spacing(0, 0, 2),
    },
  },
  toolbarDesktop: {
    padding: '0px',
    minHeight: 30,
  },
  toolbarMain: {
    padding: '0px',
    minHeight: 60,
  },
  toolbarSecondary: {
    padding: '0px',
    minHeight: 50,
  },
  toolbarPromotion: {
    padding: '0px',
    minHeight: 50,
  },
  svg: {
    fill: '#fff',
  },
  menuList: {
    display: 'flex',
    flexDirection: 'row',
    padding: '0',
  },
  menuListItem: {
    padding: 0,
    paddingRight: 20,
    textTransform: 'capitalize',
  },
  listItemLink: {
    fontSize: 13,
    color: '#fff',
    textDecoration: 'none',
  },
}));

// کامپوننت سفارشی برای آیتم‌های لیست منو
const DokoonListItem = forwardRef((props, ref) => { // Renamed to DokoonListItem
  return <li ref={ref} {...props} />;
});

// کامپوننت اصلی هدر
export default function Header({ data }) {
  const classes = useDokoonStyles();
  const listItemRef = useRef();

  useEffect(() => {
    // اگر رفرنس آیتم لیست وجود داشته باشد، در اینجا می‌توانیم با DOM کار کنیم
    if (listItemRef.current) {
      console.log(listItemRef.current);
    }
  }, [listItemRef]);

  return (
    <nav>
      <AppBar position="relative" elevation={0} className={classes.appbarDesktop}>
        <Container maxWidth="lg">
          <Toolbar className={classes.toolbarDesktop}></Toolbar>
        </Container>
      </AppBar>
      <AppBar position="static" elevation={0} className={classes.appbarMain}>
        <Container maxWidth="lg">
          <Toolbar className={classes.toolbarMain}>
            <Link href="/" passHref legacyBehavior>
              <a>
                <svg
                  className={classes.svg}
                  xmlns="http://www.w3.org/2000/svg"
                  width="120"
                  height="50"
                  viewBox="23 0 476 140"
                >
                  <text x="82" y="90" fontSize="90" fill="white">
                    DOKOON
                  </text>
                </svg>
              </a>
            </Link>
          </Toolbar>
        </Container>
      </AppBar>
      <AppBar position="relative" elevation={0} className={classes.appbarSecondary}>
        <Container maxWidth="lg">
          <Toolbar className={classes.toolbarSecondary}>
            <List className={classes.menuList}>
              {data.map((category) => (
                <DokoonListItem key={category.name} className={classes.menuListItem} ref={listItemRef}> {/* Using DokoonListItem */}
                  <Link href={`/category/${encodeURIComponent(category.slug)}`} passHref legacyBehavior>
                    <a className={classes.listItemLink}>{category.name}</a>
                  </Link>
                </DokoonListItem>
              ))}
            </List>
          </Toolbar>
        </Container>
      </AppBar>
      <AppBar position="relative" elevation={0} className={classes.appbarPromotion}>
        <Container maxWidth="lg">
          <Toolbar className={classes.toolbarPromotion}></Toolbar>
        </Container>
      </AppBar>
    </nav>
  );
}