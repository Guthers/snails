import React from 'react';

import Avatar from '@material-ui/core/Avatar';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardMedia from '@material-ui/core/CardMedia';
import CardContent from '@material-ui/core/CardContent';
import CardActions from '@material-ui/core/CardActions';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';
import FavoriteIcon from '@material-ui/icons/Favorite';
import ReplyIcon from '@material-ui/icons/Reply';

import { red } from '@material-ui/core/colors';
import { makeStyles } from '@material-ui/core/styles';
import { Badge, createGenerateClassName, IconButton } from '@material-ui/core';

const useStyles = makeStyles((theme) => ({
  root: {
    marginTop: '2em',
    padding: '1.5em 1.25em',
    paddingBottom: '1.00em'
  },
  avatar: {
    backgroundColor: red[500],
  },
  leftSpace: {
    marginLeft: '5px',
  },
}));

type Props = {
  name: string,
  username: string,
  numLikes: number,
  numReplies: number,
  content: string,
};

const Post: React.FC<Props> = (props) => {
  const classes = useStyles();

  const PostActions = (
    <Box marginTop="0.5em">
      <IconButton>
        <FavoriteIcon/>
      </IconButton>
      {props.numLikes}
      <IconButton>
        <ReplyIcon/>
      </IconButton>
      {props.numReplies}
    </Box>
  );

  return (
    <Card className={classes.root}>
      <Box display="flex">
        <Avatar aria-label="avatar" className={classes.avatar}>
          {props.name.split(' ').map(x => x[0]).join('')}
        </Avatar>
        <Box>
          <Box marginLeft="1em">
            <Box alignItems="center" display="flex" marginBottom="0.5em">
              <Box fontWeight="fontWeightBold">
                {props.name}
              </Box>
              <Typography variant="subtitle2" className={classes.leftSpace}>
                @{props.username}
              </Typography>
            </Box>
            <Typography variant="body2" color="textPrimary" component="p">
              {props.content}
            </Typography>
          </Box>
          {PostActions}
        </Box>
      </Box>
    </Card>
  );
}

export default Post;