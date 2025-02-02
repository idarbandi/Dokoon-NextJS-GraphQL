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
import { gql } from '@apollo/client';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Box from '@material-ui/core/Box';
import Hidden from '@material-ui/core/Hidden';
import Typography from '@material-ui/core/Typography';
import { DokoonProductSlug } from '../graphQL/graphQL';

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
  const classes = useDokoonProductStyles();
  const router = useRouter();

  if (router.isFallback) {
    return <Typography>در حال بارگذاری...</Typography>;
  }

  if (!post || Object.keys(post).length === 0) {
    return <Typography>محصولی یافت نشد.</Typography>;
  }

  return (
    <>
      <Head>
        <title>{post.title}</title>
      </Head>
      <Header data={categories} />
      <Container>
        <Grid container spacing={3}>
          <Grid item xs={12} sm={6}>
            <Paper className={classes.paperImagePreview}>
              <img
                className={classes.img}
                src={post.productImage?.[0]?.image || '/default-image.jpg'}
                alt={post.productImage?.[0]?.altText || post.title}
              />
            </Paper>
          </Grid>
          <Grid item xs={12} sm={6}>
            <Box className={classes.paperRight}>
              <Typography variant="h4">{post.title}</Typography>
              <Typography variant="body1">{post.description}</Typography>
            </Box>
          </Grid>
        </Grid>
      </Container>
    </>
  );
}

export async function getStaticPaths() {
  let paths = [];

  try {
    const { data } = await client.query({
      query: gql`
        query {
          allSlugs
        }
      `,
    });

    paths = data.allSlugs.map((slug) => ({
      params: { slug },
    }));
  } catch (error) {
    // console.error('Error fetching paths:', error);
  }

  return {
    paths,
    fallback: true,
  };
}

export async function getStaticProps({ params }) {
  let post = {};
  let categories = [];

  try {
    const { data } = await DokoonProductSlug(params.slug);
    post = data.mainIndexByName;

    // If you need to fetch categories, you can do it here
    // const categoriesData = await client.query({ /* your categories query */ });
    // categories = categoriesData.data.categories;

    console.log('GraphQL data:', data);
  } catch (error) {
    console.error('Error fetching data:', error);
    return {
      notFound: true,
    };
  }

  return {
    props: {
      post,
      categories,
    },
    revalidate: 10,
  };
}

export default ProductPage;
