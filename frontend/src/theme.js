import { createTheme } from '@mui/material/styles'; // Import from @mui/material/styles

const theme = createTheme({
  // Use createTheme from MUI v5
  palette: {
    primary: {
      main: '#FF5733', // A fiery orange-red
      light: '#FF8566', // A lighter shade for contrast
      dark: '#C73E1D', // A darker shade for contrast
    },
    secondary: {
      main: '#00BCD4', // A bright cyan
      light: '#4dd0e1',
      dark: '#0097a7',
    },
    error: {
      main: '#F44336', // Standard red for errors
    },
    warning: {
      main: '#FFC107', // Amber for warnings
    },
    info: {
      main: '#2196F3', // Blue for info
    },
    success: {
      main: '#4CAF50', // Green for success
    },
    background: {
      default: '#121212', // Dark background
      paper: '#1E1E1E', // Darker shade for paper elements
    },
    text: {
      primary: '#FFFFFF', // White text for contrast on dark background
      secondary: '#BDBDBD', // A lighter gray for secondary text
    },
  },
  typography: {
    fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif', // Standard font stack
    h1: {
      fontWeight: 700,
    },
    h2: {
      fontWeight: 600,
    },
    h3: {
      fontWeight: 500,
    },
    // ... other typography styles
  },
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: '8px', // Slightly rounded buttons
          textTransform: 'none', // Prevent uppercase transformation
        },
      },
    },
    MuiPaper: {
      styleOverrides: {
        root: {
          borderRadius: '8px', // Rounded corners for paper elements
        },
      },
    },
    MuiAppBar: {
      styleOverrides: {
        root: {
          backgroundColor: '#212121', // Darker app bar color
        },
      },
    },
  },
});

export default theme;
