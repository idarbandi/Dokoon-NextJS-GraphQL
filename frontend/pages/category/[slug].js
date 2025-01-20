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
import Header from '../../components/header';
import Box from '@material-ui/core/Box';
import CardMedia from '@material-ui/core/CardMedia';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Link from 'next/link';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import { useRouter } from 'next/router';

// استایل‌های این صفحه
const useDokoonStyles = makeStyles((theme) => ({
  example: { // This is unused, consider removing
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
    paddingTop: '140%', // Aspect ratio for images
  },
}));

// کامپوننت اصلی صفحه دسته‌بندی
function CategoryPage({ posts, categories }) { // More descriptive component name
  const classes = useDokoonStyles();
  const router = useRouter();

  if (router.isFallback) {
    return <div>در حال بارگذاری...</div>; // Persian loading message
  }

  return (
    <>
      <Header data={categories} />
      <main>
        <Container className={classes.cardGrid} maxWidth="lg">
          <Grid container spacing={2}>
            {/* نمایش اطلاعات محصولات در کنسول (برای دیباگ) */}
            {console.log(posts)}
            {posts.map((post) => (
              <Link legacyBehavior key={post.id} href={`/product/${encodeURIComponent(post.slug)}`}>
                <Grid item xs={6} sm={4} md={3}>
                  <Card className={classes.card} elevation={0}>
                    <CardMedia
                      className={classes.cardMedia}
                      image={post.product_image[0]?.image || "/images/default.png"} // Handling potential missing images
                      title={post.title} // Use post title for image title
                      alt={post.product_image[0]?.alt_text || "تصویر محصول"} // Default alt text in Persian
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

// دریافت مسیرهای استاتیک
export async function getStaticPaths() {
  return {
    paths: [{ params: { slug: 'shoes' } }], // You should fetch this dynamically in a real app.
    fallback: true,
  };
}

// دریافت اطلاعات استاتیک
export async function getStaticProps({ params }) {
  try { // Added try-catch for error handling
    const res = await fetch(`http://127.0.0.1:8000/api/category/${params.slug}`);
    const posts = await res.json();

    const ress = await fetch('http://127.0.0.1:8000/api/category/');
    const categories = await ress.json();

    return {
      props: {
        posts,
        categories,
      },
      revalidate: 10, // Revalidate every 10 seconds (adjust as needed)
    };
  } catch (error) {
    console.error("Error fetching data:", error);
    return {
      props: {
        posts: [],
        categories: [],
      },
    };
  }
}

export default CategoryPage; // Export with the new name