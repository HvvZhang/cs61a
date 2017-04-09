.read sp16data.sql
.read fa16data.sql

CREATE TABLE obedience AS
  select seven, denero from students;

CREATE TABLE smallest_int AS
  select time, smallest from 
  	students where smallest > 8  order by smallest limit 20;

CREATE TABLE greatstudents AS
  select s1.date, s1.number, s1.pet, s1.color, s2.color from
  	students as s1, sp16students as s2 where 
  	s1.date = s2.date and s1.number = s2.number and s1.pet = s2.pet;

CREATE TABLE sevens AS
  select seven from 
  	students as s, checkboxes as c where 
  	s.number = 7 and c."7" = "True" and s.time = c.time;

CREATE TABLE matchmaker AS
  select s1.pet, s1.song, s1.color, s2.color from 
  	students as s1, students as s2 where
  	s1.pet = s2.pet and s1.song = s2.song and s1.time < s2.time;
