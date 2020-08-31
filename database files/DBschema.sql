/*Tables for the database*/


/*Creates a table to user informtation*/
CREATE TABLE USER (
  studentID INT PRIMARY KEY,
  name VARCHAR(225 BYTE),
  username VARCHAR(225 BYTE),
  getMessages VARCHAR(225 BYTE),
  userCreateDate VARCHAR(225 BYTE),
);


/*Creates a table to store message information*/
CREATE TABLE MESSAGE (
  messageID INT;
  messageContent VARCHAR(225 BYTE),
  createDate VARCHAR(225 BYTE),
  getFromUserID VARCHAR(225 BYTE),        //Get the user who sent the message
  getToUserID VARCHAR(225 BYTE)           //Get the user who received the message
);


/*Creates a table to store post information*/
CREATE TABLE POST (
  postID INT;
  postContent VARCHAR(225 BYTE),
  createDate VARCHAR(225 BYTE),
  getUserId VARCHAR(225 BYTE),        //Get the user who posted the message
  getUserResponses VARCHAR(225 BYTE)  //Get all the users who responded
  
);


