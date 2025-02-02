import { gql, ApolloClient, InMemoryCache } from '@apollo/client';

const client = new ApolloClient({
  uri: 'http://127.0.0.1:8000/graphQl/',
  cache: new InMemoryCache(),
});

export default client;

export async function DokoonIndexData() {
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

export const LoginMutation = gql`
  mutation TokenAuth($username: String!, $password: String!) {
    tokenAuth(username: $username, password: $password) {
      token
      payload
    }
  }
`;

export const userDetails = gql`
  query {
    userDetails {
      id
      username
      email
    }
  }
`;

export const LOGOUT_MUTATION = gql`
  mutation Logout {
    logout {
      success
      errors
    }
  }
`;

export async function DokoonProductSlug(slug) {
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
      }
    `,
    variables: { slug },
  });
}

export async function DokoonCategorySlug(name) {
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
      }
    `,
    variables: { name },
  });
  return data;
}
