import React from 'react';
import './App.css';

import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';

import Bar from './Bar';
import Post from './Post';
import { useStoreState } from './hooks';
import { Fab } from '@material-ui/core';
import AddIcon from '@material-ui/icons/Add';

function App() {
  const [value, setValue] = React.useState(0);
  const posts = useStoreState(state => state.posts.items);
  return (
    <Box display="flex" flexDirection="column" height="100vh">
        <Bar/>
        <Container >
          <Box paddingTop="2em">
            {posts.map((post) => 
              <Post name={post.author.name} 
                    username={post.author.username} 
                    numLikes={post.liked_by.length}
                    numReplies={post.replies.length}
                    content={post.content}
                    
              />)
            }
          </Box>
          <Box position="absolute" marginBottom="2rem" marginRight="1rem" bottom="0" right="0">
            <Fab color="primary" aria-label="add">
              <AddIcon />
            </Fab>
          </Box>
        </Container>
    </Box>
  );
}

export default App;
