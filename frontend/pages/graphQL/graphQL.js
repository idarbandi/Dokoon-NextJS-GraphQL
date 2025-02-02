// graphQL/graphQL.js
import { ApolloClient, InMemoryCache, createHttpLink, gql } from '@apollo/client';

/**
 * ********************************************************************************
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

// این فایل برای ارتباط با GraphQL API استفاده می‌شود

const httpLink = createHttpLink({
  uri: 'http://127.0.0.1:8000/graphQl/',
  credentials: 'include',
});

const client = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache(),
});

export default client;

// کوئری برای دریافت جزئیات کاربر
export const dokoonUserDetails = gql`
  query UserDetails {
    userDetails {
      id
      username
      email
    }
  }
`;

// Mutation برای ورود کاربر
export const dokoonLoginMutation = gql`
  mutation TokenAuth($username: String!, $password: String!) {
    tokenAuth(username: $username, password: $password) {
      token
      payload
    }
  }
`;

// Mutation برای خروج کاربر
export const dokoonLogoutMutation = gql`
  mutation Logout {
    logout {
      success
      errors
    }
  }
`;

// کوئری برای دریافت داده‌های اصلی
export async function dokoonIndexData() {
  return await client.query({
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
}

// کوئری برای دریافت داده‌های یک محصول بر اساس اسلاگ
export async function dokoonProductSlug(slug) {
  return await client.query({
    query: gql`
      query main_index_by_name($slug: String!) {
        mainIndexByName(slug: $slug) {
          id
          title
          description
          productImage {
            id
            image
            altText
          }
        }
      `,
    variables: { slug },
  });
}

// کوئری برای دریافت داده‌های یک دسته‌بندی بر اساس نام
export async function dokoonCategorySlug(name) {
  const { data } = await client.query({
    query: gql`
      query category_index_by_name($name: String!) {
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
      `,
    variables: { name },
  });
  return data;
}
