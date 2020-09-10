import { PostModel, AuthorModel } from "../model/post";

const amityAuthor: AuthorModel =
  {
    "created_at": "string",
    "name": "Amity Blight",
    "user_id": 0,
    "username": "amityblight",
  }
const belosAuthor: AuthorModel =
  { "created_at": "string",
    "name": "Emperor Belos",
    "user_id": 1,
    "username": "kingofthebi",
  }
const kingAuthor: AuthorModel =
  { "created_at": "string",
    "name": "King",
    "user_id": 2,
    "username": "billcipher",
  }
const gusAuthor: AuthorModel =
  { "created_at": "string",
    "name": "Gus",
    "user_id": 3,
    "username": "itsgus",
  }

const amityContent: string[] = [
  "I bet you did. I've got my eyes on you, Half-a-Witch. That badge is mine.",
  "Lets see what kind of witch you are.",
  "Shut up.",
  "Me, on a team- with you? Running around in cute uniforms- sweating? I gotta go!"
];
const belosContent: string[] = [
  "I bet you did. I've got my eyes on you, Half-a-Witch. That badge is mine.",
  "Lets see what kind of witch you are.",
  "Shut up.",
  "Me, on a team- with you? Running around in cute uniforms- sweating? I gotta go!"
];
const kingContent: string[] = [
  "Bap!",
  "The King of Demons is back!",
  "Finally, all that mean-spirited laughter made me sleepy",
  "That was actually one of her better breakups"
];
const gusContent: string[] = [
  "Should i turn to forbidden sources?",
];

//export const retrieve: PostModel[] = (n: number) => 
//  new Promise(
//    setTimeout(resolve, 750);
//  })