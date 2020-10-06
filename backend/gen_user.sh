#!/usr/bin/env sh

sqlite3 test.db <<'END_SQL'
.timeout 2000
insert into userdb (student_id,student_name) values ('s4430265', 'Joshua Hwang');
insert into userdb (student_id,student_name) values ('s1234567', 'Rudolph Red');
insert into userdb (student_id,student_name) values ('s7392740', 'John Dove');
insert into userdb (student_id,student_name) values ('s3720482', 'James Bond');
insert into userdb (student_id,student_name) values ('s4729057', 'Amy Bond');
insert into userdb (student_id,student_name) values ('s8205893', 'Becky Carol');
END_SQL
