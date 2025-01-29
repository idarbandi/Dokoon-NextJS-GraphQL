/** ********************************************************************************
 * Dokoon Project
 * Author: Idarbandi
 * GitHub: https://github.com/idarbandi/Dokoon-NextDRF
 * Email: darbandidr99@gmail.com
 *
 * This project was developed by Idarbandi.
 * We hope you find it useful! Contributions and feedback are welcome.
 * ****************************************************************************** */

import React from 'react';
import Head from 'next/head';
import { useRouter } from 'next/router';
import DokoonHeader from '../../components/header';
import Container from '@material-ui/core/Container';
import { gql } from '@apollo/client';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';
import client from '../api/apollo-client';
import Link from 'next/link';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';

// استایل‌های این صفحه (با نام DokoonCategory)
const useDokoonCategoryStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  cardGrid: {
    paddingTop: theme.spacing(8),
    paddingBottom: theme.spacing(8),
  },
  card: {
    display: 'flex',
    flexDirection: 'column',
    backgroundColor: '#fafafa',
  },
  cardMedia: {
    paddingTop: '56.25%',
  },
  cardContent: {
    flexGrow: 1,
  },
}));

// کامپوننت صفحه دسته‌بندی
const CategoryPage = ({ category, posts }) => {
  const classes = useDokoonCategoryStyles();
  const router = useRouter();

  if (router.isFallback) {
    return <Typography>در حال بارگذاری...</Typography>;
  }

  if (!category) {
    return <Typography>دسته بندی یافت نشد.</Typography>;
  }

  return (
    <>
      <Head>
        <title>{category.name}</title>
      </Head>
      <DokoonHeader data={[category]} /> {/* Pass category as array */}
      <main>
        <Container className={classes.cardGrid} maxWidth="lg">
          <Grid container spacing={2}>
            {posts?.map((post, index) => (
              <Link legacyBehavior key={post.id || index} href={`/product/${encodeURIComponent(post.slug)}`}>
                <Grid item xs={6} sm={4} md={3}>
                  <Card className={classes.card} elevation={0}>
                    <CardMedia
                      className={classes.cardMedia}
                      image={post.productImage[0]?.image}
                      title={post.title}
                      alt={post.productImage[0]?.altText || 'تصویر محصول'}
                    />
                    <CardContent className={classes.cardContent}>
                      <Typography gutterBottom component="p">
                        {post.title}
                      </Typography>
                      <Box component="p" fontSize={16} fontWeight={900}>
                        £{post.regularPrice}
                      </Box>
                    </CardContent>
                  </Card>
                </Grid>
              </Link>
            ))}
          </Grid>
        </Container>
      </main>
    </>
  );
};

export async function getStaticPaths() {
  let paths = [];

  try {
    const query = gql`
      query {
        allSlugs
      }
    `;
    const { data } = await client.query({ query });

    paths = data.allSlugs.map((slug) => ({
      params: { slug },
    }));
  } catch (error) {
    console.error('Error fetching paths:', error);
  }

  return {
    paths,
    fallback: true,
  };
}

export async function getStaticProps({ params }) {
  let category = null;
  let posts = [];

  try {
    const query = gql`
      query MyQuery($name: String!) {
        categoryIndexByName(name: $name) {
          id
          name
          productCategory {
            id
            title
            description
            regularPrice
            productImage {
              id
              image
              altText
            }
          }
        }
      }
    `;
    const variables = { name: params.slug };
    console.log('Fetching data with variables:', variables); // Add logging
    const { data } = await client.query({ query, variables });

    console.log('Received data:', data); // Add logging

    category = data.categoryIndexByName;
    posts = category?.productCategory || [];
  } catch (error) {
    console.error('Error fetching data:', error.message);
    return {
      notFound: true,
    };
  }

  return {
    props: {
      category,
      posts,
    },
    revalidate: 10,
  };
}

export default CategoryPage;
