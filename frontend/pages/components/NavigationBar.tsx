import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';

export default function NavigationBar() {
  return (
    <React.Fragment>
      <CssBaseline />
      <Container style={{"width": "100vw"}}>
        <Box sx={{ bgcolor: '#8282B2', height: '100vh' }}>
          Hello
        </Box>
      </Container>
    </React.Fragment>
  );
}