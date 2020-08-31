/*Tables for the database: USER, ENTRY (POSTS), MESSAGE, REPLY, TO*/

/*Specifications: 
Get messages of a user via userID
Get posts of a user via userID 
getUserResponses VARCHAR(225 BYTE),     //Get all the users who wrote a response
LikedBy VARCHAR(225 BYTE)              //Get all the users who liked the post
*/


/*Table that stores user informtation*/
CREATE TABLE USER (
  studentID INT PRIMARY KEY,
  name VARCHAR(225 BYTE),
  bio VARCHAR(225 BYTE),
  userCreateDate VARCHAR(225 BYTE)
);

/*Table that stores an entry/post information*/
CREATE TABLE ENTRY (
  postID INT PRIMARY KEY,
  postContent VARCHAR(225 BYTE),
  createDate DATE,
  getAuthorID INT,                        //Get the authorID of the post
  getAuthor VARCHAR(225 BYTE),           
);


/*Table to store private messaging information*/
CREATE TABLE MESSAGE (
  messageID INT PRIMARY KEY;
  messageContent VARCHAR(225 BYTE),
  createDate DATE,
  FromUserID INT,                        //Get userID who sent the message
  ToUserID INT,                          //Get userID who received the message
  FromUserName VARCHAR(225 BYTE),        //Get userName who sent the message
  ToUserName VARCHAR(225 BYTE)           //Get userName who received the message
);

/*Table to store a reply:
This allows us to get all responses to a post*/
CREATE TABLE REPLY (
  postID INT,
  userID INT,
  createDate DATE,
  RepliedToName VARCHAR(225 BYTE)
);

/*Table to store a reply:
This allows us to get all people who liked a post*/
CREATE TABLE LIKED (
  postID INT,
  UserID INT,
  createDate DATE
);





