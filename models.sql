/*
-- Query: SELECT * FROM books.books
LIMIT 0, 1000

-- Date: 2019-11-11 18:33
*/
CREATE DATABASE  IF NOT EXISTS `books` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `books`;

create table users (UsersID char(12) not NULL,name varchar(5) default NULL,password varchar(8) default NULL,email varchar(20) default NULL,phonenumber varchar(12) default NULL,primary key(UsersID))engine=InnoDB default charset=utf8;
create table administors (adminID char(12) not NULL,name varchar(5) default NULL,password varchar(8) default NULL,email varchar(20) default NULL,primary key(adminID))engine=InnoDB default charset=utf8;
create table book (bookID char(12) not NULL,name varchar(20) default NULL,publisher varchar(8) default NULL,publishtime date default NULL,edition int default NULL,author varchar(20) default NULL,stock int default NULL,primary key(bookID))engine=InnoDB default charset=utf8;

insert into book values('4N10001','数据库系统概念','机械工业出版社','2012-11-01',6,'S.Sudarshan',3);
create table seat (seatID char(12) not NULL,floor int default NULL,primary key(seatID))engine=InnoDB default charset=utf8;
create table room (roomID char(12) not NULL,numlimit int default NULL,uses varchar(8) default NULL,service varchar(20) default NULL,primary key(roomID))engine=InnoDB default charset=utf8;
create table borrowbook (BorrowID char(12) not NULL,bookID char(12) default NULL,borrowtime date default NULL,shouldbacktime date default NULL,Infactbacktime date default NULL,backyon char(1) default NULL,breakyon char(1) default NULL,primary key(BorrowID))engine=InnoDB default charset=utf8;

Insert into borrowbook values('000000000001','4N10001','2013-01-01','2013-02-01','2013-01-16','是','否');
create table useroom (UseroomID char(12) not NULL,roomID char(12) default NULL,freeyon 
varchar(5) default NULL,primary key(UseroomID))engine=InnoDB default charset=utf8;
create table useseat (UseseatID char(12) not NULL,seatID char(12) default NULL,freeyon varchar(5) default NULL,primary key(UseseatID))engine=InnoDB default charset=utf8;
