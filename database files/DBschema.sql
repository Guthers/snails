/*Tables for the database: USER, ENTRY (POSTS), MESSAGE*/


/*Creates a table to user informtation*/
CREATE TABLE USER (
  studentID INT PRIMARY KEY,
  name VARCHAR(225 BYTE),
  username VARCHAR(225 BYTE),
  getMessages VARCHAR(225 BYTE),
  userCreateDate VARCHAR(225 BYTE),
);

/*Creates a table to store an entry (post) information*/
CREATE TABLE ENTRY(
  postID INT PRIMARY KEY,
  postContent VARCHAR(225 BYTE),
  createDate VARCHAR(225 BYTE),
  getAuthorID INT,
  getAuthor VARCHAR(225 BYTE),         //Get the author of the post
  getUserResponses VARCHAR(225 BYTE),  //Get all the users who wrote a response
  LikedBy VARCHAR(225 BYTE),           //Get all the users who liked the post
);


/*Creates a table to store private messaging information*/
CREATE TABLE MESSAGE (
  messageID INT PRIMARY KEY;
  messageContent VARCHAR(225 BYTE),
  createDate VARCHAR(225 BYTE),
  getFromUserID VARCHAR(225 BYTE),        //Get the user who sent the message
  getToUserID VARCHAR(225 BYTE)           //Get the user who received the message
);





