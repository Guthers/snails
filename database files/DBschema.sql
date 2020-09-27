/*Tables for the database: USER, ENTRY (POSTS), MESSAGE, REPLY, TO*/

/*Specifications: 
Get messages of a user via userID
Get posts of a user via userID 
*/

/*Table that stores user informtation*/
CREATE TABLE USER (
  studentID INT NOT NULL,
  studentName VARCHAR(255 BYTE),
  bio VARCHAR(255 BYTE),
  userCreateDate DATE,
  PRIMARY KEY (studentID)
);

/*Table that stores an entry/post information*/
CREATE TABLE EPOST (
  postID INT NOT NULL,
  authorID INT NOT NULL,
  content VARCHAR(255 BYTE),
  createDate DATE,
  likeCount INT,
  PRIMARY KEY (postID),
  FOREIGN KEY (authorID) REFERENCES USER(studentID)
);


/*Table to store private messaging information*/
CREATE TABLE UMESSAGE (
  messageID INT NOT NULL;
  messageContent VARCHAR(255 BYTE),
  createDate DATE,
  fromUserID INT,                        /*Get userID who sent the message*/
  toUserID INT,                          /*Get userID who received the message*/
  PRIMARY KEY (messageID),
  FOREIGN KEY (fromUserID) REFERENCES USER(studentID),
  FOREIGN KEY (toUserID) REFERENCES USER(studentID)
);

/*Table to store a reply:
This allows us to get all responses to a post*/
CREATE TABLE REPLY (
  replyID INT NOT NULL,
  postID INT,
  userID INT,
  createDate DATE,
  response VARCHAR(255 BYTE) //The string that's a response to a post
  PRIMARY KEY (replyID),
  FOREIGN KEY (postID) REFERENCES POST(postID),
  FOREIGN KEY (userID) REFERENCES USER(studentID)
);

/*Table to store likes:
This allows us to get all people who liked a post*/
CREATE TABLE LIKED (
  postID INT,
  UserID INT,
  createDate DATE,
  FOREIGN KEY (postID) REFERENCES POST(postID),
  FOREIGN KEY (userID) REFERENCES USER(studentID)
);


/*Table to store the actual information boards (Used for the showing maps with respect to positions)*/
CREATE TABLE BOARD (
  boardID INT NOT NULL,
  longitude FLOAT,
  latitude FLOAT,
  PRIMARY KEY (boardID) 
);

