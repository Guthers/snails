import { Action, action, Thunk, thunk } from "easy-peasy";

export interface PostsModel {
  items: PostModel[],
  retrievedPosts: Action<PostsModel, PostModel[]>,
  retrievePosts: Thunk<PostsModel, number>,
}

export interface PostModel {
  content: string
  created_at: string
  entry_id: string
  liked_by: AuthorModel[]
  replies: string[]
  reply_to?: string
  author: AuthorModel
};

export interface AuthorModel {
  created_at: string
  name: string
  user_id: number
  username: string
};

const items: PostModel[] = [
  {
    "author": {
      "created_at": "2020-09-07T05:14:56.803Z",
      "name": "Melissa McEwen",
      "user_id": 1,
      "username": "melissamcewen"
    },
    "content": "Writing a horror book called “Chores you didn’t know existed and were supposed to be doing all along“",
    "created_at": "2020-09-07T05:14:56.803Z",
    "entry_id": "string",
    "liked_by": [
      {
        "created_at": "2020-09-07T05:14:56.803Z",
        "name": "string",
        "user_id": 0,
        "username": "string"
      }
    ],
    "replies": [
      "string"
    ],
    "reply_to": "string"
  },
  {
    "author": {
      "created_at": "2020-09-07T05:14:56.803Z",
      "name": "SwiftOnSecurity",
      "user_id": 1,
      "username": "SwiftOnSecurity"
    },
    "content": "1.) Affresh clothes washer cleaner.~\n\
2.) Gently cleaning TV/computer screens. Even dust you can’t see can futz the image a bit.~\n\
3.) THE DISHWASHER FILTER",
    "created_at": "2020-09-07T05:14:56.803Z",
    "entry_id": "string",
    "liked_by": [
      {
        "created_at": "2020-09-07T05:14:56.803Z",
        "name": "string",
        "user_id": 0,
        "username": "string"
      }
    ],
    "replies": [
      "string"
    ],
    "reply_to": "string"
  },
  {
    "author": {
      "created_at": "2020-09-07T05:14:56.803Z",
      "name": "Amity Blight",
      "user_id": 1,
      "username": "luz4ever"
    },
    "content": "shut up.",
    "created_at": "2020-09-07T05:14:56.803Z",
    "entry_id": "string",
    "liked_by": [
      {
        "created_at": "2020-09-07T05:14:56.803Z",
        "name": "string",
        "user_id": 0,
        "username": "string"
      }
    ],
    "replies": [
      "string"
    ],
    "reply_to": "string"
  },
  {
    "author": {
      "created_at": "2020-09-07T05:14:56.803Z",
      "name": "Amity Blight",
      "user_id": 1,
      "username": "luz4ever"
    },
    "content": "shut up.",
    "created_at": "2020-09-07T05:14:56.803Z",
    "entry_id": "string",
    "liked_by": [
      {
        "created_at": "2020-09-07T05:14:56.803Z",
        "name": "string",
        "user_id": 0,
        "username": "string"
      }
    ],
    "replies": [
      "string"
    ],
    "reply_to": "string"
  },
];

const postsModel: PostsModel = {
  items: items,
  // concatenate newly retrieved post with the old posts
  retrievedPosts: action((state, posts) => {
    state.items.concat(posts)
  }),
  // retrieve the n most recent posts
  retrievePosts: thunk(async (actions, n) => {
  })
}

export default postsModel;