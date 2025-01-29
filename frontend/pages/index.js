/** ********************************************************************************
 * Dokoon Project
 * Author: Idarbandi
 * GitHub: https://github.com/idarbandi/Dokoon-NextDRF
 * Email: darbandidr99@gmail.com
 *
 * This project was developed by Idarbandi.
 * We hope you find it useful! Contributions and feedback are welcome.
 * ****************************************************************************** */

import { makeStyles } from '@material-ui/core/styles';
import DokoonHeader from '../components/header';
import Box from '@material-ui/core/Box';
import CardMedia from '@material-ui/core/CardMedia';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Link from 'next/link';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import { gql } from '@apollo/client';
import client from './api/apollo-client';

// استایل‌های صفحه اصلی
const useDokoonHomeStyles = makeStyles((theme) => ({
  example: {
    color: '#ccc',
  },
  cardGrid: {
    paddingBottom: theme.spacing(8),
  },
  card: {
    height: '100%',
    display: 'flex',
    flexDirection: 'column',
    borderRadius: '0',
  },
  cardMedia: {
    paddingTop: '140%',
  },
}));

// کامپوننت صفحه اصلی
function DokoonHome({ posts, categories }) {
  console.log(posts)
  const classes = useDokoonHomeStyles();

  return (
    <>
      <DokoonHeader data={categories} /> {/* Pass categories to DokoonHeader */}
      <main>
        <Container className={classes.cardGrid} maxWidth="lg">
          <Grid container spacing={2}>
            {posts?.map((post, index) => (
              <Link legacyBehavior key={post.id || index} href={`product/${post.slug}`}>
                <Grid item xs={6} sm={4} md={3}>
                  <Card className={classes.card} elevation={0}>
                    <CardMedia
                      className={classes.cardMedia}
                      image={post.productImage[0].image}
                      title={post.title}
                      alt={
                        post.product_image?.[0]?.alt_text || 'تصویر محصول'
                          ? post.product_image?.[0]?.alt_text || 'تصویر محصول'
                          : post.productImage[0].altText || 'تصویر محصول'
                      }
                    />
                    <CardContent>
                      <Typography gutterBottom component="p">
                        {post.title}
                      </Typography>
                      <Box component="p" fontSize={16} fontWeight={900}>
                        £{post.regularPrice} {/* Updated to regularPrice */}
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
}

// دریافت اطلاعات استاتیک
export async function getStaticProps() {
  let posts = [];
  let categories = [];

  try {
    const { data } = await client.query({
      query: gql`
        query main_index {
          mainIndex {
            description
            id
            slug
            title
            productImage {
              id
              image
              altText
            }
            regularPrice
          }
          categoryIndex {
            id
            name
          }
        }
      `,
    });

    posts = data.mainIndex;
    categories = data.categoryIndex;

    console.log('GraphQL data:', data);
  } catch (error) {
    console.error('Error fetching data:', error);
  }

  return {
    props: {
      posts,
      categories,
    },
    revalidate: 10,
  };
}

export default DokoonHome;



