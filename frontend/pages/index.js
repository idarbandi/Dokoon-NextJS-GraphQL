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
  // Renamed to DokoonHome
  const classes = useDokoonHomeStyles();

  return (
    <>
      <DokoonHeader data={categories} />
      <main>
        <Container className={classes.cardGrid} maxWidth="lg">
          <Grid container spacing={2}>
            {posts?.map((post, index) => (
              <Link legacyBehavior key={post.id || index} href={`product/${encodeURIComponent(post.slug)}`}>
                <Grid item xs={6} sm={4} md={3}>
                  <Card className={classes.card} elevation={0}>
                    <CardMedia
                      className={classes.cardMedia}
                      image={post.product_image?.[0]?.image || '/images/default.png'}
                      title={post.title}
                      alt={post.product_image?.[0]?.alt_text || 'تصویر محصول'}
                    />
                    <CardContent>
                      <Typography gutterBottom component="p">
                        {post.title}
                      </Typography>
                      <Box component="p" fontSize={16} fontWeight={900}>
                        £{post.regular_price}
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
  try {
    const res = await fetch('http://127.0.0.1:8000/api/محصولات/');
    const posts = await res.json();

    const ress = await fetch('http://127.0.0.1:8000/api/دسته-بندی‌ها/');
    const categories = await ress.json();

    return {
      props: {
        posts,
        categories,
      },
      revalidate: 10,
    };
  } catch (error) {
    console.error('Error fetching data:', error);
    return {
      props: {
        posts: [],
        categories: [],
      },
    };
  }
}

export default DokoonHome; // Export is also renamed
