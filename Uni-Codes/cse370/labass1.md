#Task 1
alter table users rename column influence_count to followers; alter table users modify followers int(40);

#Task 2
alter table users rename column member_since to joining_date; alter table users modify joining_date date;

#Task 3
select name, email, followers from users;

#Task 4
select * , ((followers*100/1000000) * (multiplier*100/20))/100 as Efficiency from users;

#Task 5
alter table users modify column multiplier varchar(20);
