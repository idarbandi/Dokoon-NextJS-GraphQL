/** ********************************************************************************
 * Dokoon Project
 * Author: Idarbandi
 * GitHub: https://github.com/idarbandi/Dokoon-NextDRF
 * Email: darbandidr99@gmail.com
 *
 * This project was developed by Idarbandi.
 * We hope you find it useful! Contributions and feedback are welcome.
 * ****************************************************************************** */

import Head from 'next/head';
import { useRouter } from 'next/router';
import Header from '../../components/header';
import Container from '@material-ui/core/Container';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Box from '@material-ui/core/Box';
import Hidden from '@material-ui/core/Hidden';

// استایل‌های این صفحه (با نام Dokoon)
const useDokoonProductStyles = makeStyles((theme) => ({
  // Prefixed styles
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(0),
    borderRadius: '0',
  },
  paperImagePreview: {
    paddingTop: theme.spacing(3),
  },
  paperImage: {
    padding: theme.spacing(0),
    borderRadius: '0',
    marginLeft: 25,
    marginRight: 25,
    ['@media (max-width:600px)']: {
      marginLeft: -20,
      marginRight: -20,
    },
  },
  paperRight: {
    padding: theme.spacing(0),
    borderRadius: '0',
    paddingLeft: 40,
    paddingTop: theme.spacing(3),
    ['@media (max-width:600px)']: {
      paddingLeft: 0,
      paddingTop: 10,
    },
  },
  img: {
    maxWidth: '100%',
  },
}));

// کامپوننت صفحه محصول
function ProductPage({ post, categories }) {
  const classes = useDokoonProductStyles(); // Using prefixed styles
  const router = useRouter();

  if (router.isFallback) {
    return <div>در حال بارگذاری...</div>;
  }

  return (
    <>
      <Head>
        <title>{post.title}</title>
      </Head>
      <Header data={categories} />
      <Container maxWidth="md">
        <Grid container spacing={0}>
          <Hidden only={['xs', 'sm']}>
            <Grid item sm={1}>
              <Paper className={classes.paperImagePreview} elevation={0}>
                {post.product_image?.map(
                  (
                    c,
                    index // Added index for key
                  ) => (
                    <div key={c.id || index}>
                      {' '}
                      {/* Improved key handling */}
                      <Paper className={classes.paperImage} elevation={0}>
                        <img
                          src={c.image} // Use the correct image path
                          alt={c.alt_text || 'تصویر محصول'}
                          className={classes.img}
                        />
                      </Paper>
                    </div>
                  )
                )}
              </Paper>
            </Grid>
          </Hidden>
          <Grid item xs={12} sm={6}>
            <Paper className={classes.paperImage} elevation={0}>
              <img
                src={post.product_image?.[0]?.image} // Safe navigation
                alt={post.product_image?.[0]?.alt_text || 'تصویر اصلی محصول'} // Safe navigation and Persian default
                className={classes.img}
              />
            </Paper>
          </Grid>
          <Grid item xs={12} sm={5}>
            <Paper className={classes.paperRight} elevation={0}>
              <Box component="h1" fontSize={18} fontWeight="400">
                {post.title}
              </Box>
              <Box component="p" fontSize={22} fontWeight="900" m={0}>
                £{post.regular_price}
              </Box>
              <Box component="p" m={0} fontSize={14}>
                ارسال و برگشت رایگان (شرایط اعمال می شود)
              </Box>
            </Paper>
          </Grid>
        </Grid>
      </Container>
    </>
  );
}

export async function getStaticPaths() {
  try {
    const res = await fetch(`http://127.0.0.1:8000/api/محصولات/`);
    const products = await res.json();
    const paths = products.map((product) => ({
      params: { slug: product.slug },
    }));
    return {
      paths,
      fallback: true,
    };
  } catch (error) {
    console.error('Error fetching paths:', error);
    return { paths: [], fallback: true };
  }
}

export async function getStaticProps({ params }) {
  try {
    const res = await fetch(`http://127.0.0.1:8000/api/محصول/${params.slug}/`); // Correct API endpoint
    const post = await res.json();

    const ress = await fetch('http://127.0.0.1:8000/api/دسته-بندی‌ها/');
    const categories = await ress.json();

    return {
      props: {
        post,
        categories,
      },
      revalidate: 10,
    };
  } catch (error) {
    console.error('Error fetching data:', error);
    return {
      props: {
        post: null, // Important: Set post to null in case of error
        categories: [],
      },
    };
  }
}

export default ProductPage;
