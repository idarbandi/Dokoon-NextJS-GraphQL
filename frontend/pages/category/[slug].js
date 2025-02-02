/** ********************************************************************************
 * 🌐 Dokoon-NextJS-GraphQL
 * 👤 Author: idarbandi
 * 📁 GitHub: https://github.com/idarbandi/Dokoon-NextJS-GraphQL
 * ✉️ Email: darbandidr99@gmail.com
 * 💼 LinkedIn: https://www.linkedin.com/in/amir-darbandi-72526b25b/
 * 🖥 Framework: NextJS
 *
 * This project was developed by idarbandi.
 * We hope you find it useful! Contributions and feedback are welcome.
 * ********************************************************************************
 */

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
import Link from 'next/link';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import { DokoonCategorySlug } from '../../graphQL/graphQL';
import client from '../../graphQL/graphQL';

// استایل‌های این صفحه
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
const DokoonCategoryPage = ({ category, posts }) => {
  const classes = useDokoonCategoryStyles();
  const router = useRouter();

  if (router.isFallback) {
    return <Typography>در حال بارگذاری...</Typography>;
  }

  if (!category) {
    return <Typography>دسته‌بندی یافت نشد.</Typography>;
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

// گرفتن مسیرهای استاتیک
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
    console.error('Error fetching paths:', error);
  }

  return {
    paths,
    fallback: true,
  };
}

// گرفتن داده‌های استاتیک
export async function getStaticProps({ params }) {
  let category = null;
  let posts = [];

  const name = params.slug;
  console.log('Fetching data with name:', name);

  try {
    const data = await DokoonCategorySlug(name);

    if (!data || !data.categoryIndexByName) {
      throw new Error('Category not found');
    }

    console.log('Received data:', data);

    category = data.categoryIndexByName;
    posts = category.productCategory || [];
  } catch (error) {
    console.error('Error fetching category data:', error);
    return {
      notFound: true, // این صفحه 404 را نمایش می‌دهد
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

export default DokoonCategoryPage;
