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
import { dokoonIndexData } from '../graphQL/graphQL';

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
  const classes = useDokoonHomeStyles();

  if (!posts || !categories) {
    return <Typography>در حال بارگذاری...</Typography>;
  }

  return (
    <>
      <DokoonHeader data={categories} /> {/* پاس دادن دسته‌بندی‌ها به DokoonHeader */}
      <main>
        <Container className={classes.cardGrid} maxWidth="lg">
          <Grid container spacing={2}>
            {posts.map((post, index) => (
              <Link legacyBehavior key={post.id || index} href={`product/${post.slug}`}>
                <Grid item xs={6} sm={4} md={3}>
                  <Card className={classes.card} elevation={0}>
                    <CardMedia
                      className={classes.cardMedia}
                      image={post.productImage?.[0]?.image || '/placeholder.jpg'}
                      title={post.title}
                      alt={post.productImage?.[0]?.altText || 'تصویر محصول'}
                    />
                    <CardContent>
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
}

// دریافت اطلاعات استاتیک
export async function getStaticProps() {
  let posts = [];
  let categories = [];

  try {
    const { data } = await dokoonIndexData();
    posts = data.mainIndex;
    categories = data.categoryIndex;

    console.log('داده‌های GraphQL:', data);
  } catch (error) {
    console.error('خطا در دریافت داده‌ها:', error);
    return {
      props: {
        posts: [],
        categories: [],
      },
    };
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
