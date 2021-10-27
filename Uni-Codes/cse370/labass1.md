#Task 1
alter table users rename column influence_count to followers;

#Task 2
alter table users rename column member_since to joining_date;

# Task 3
show name,name, email, followers from users;

# Task 4

show * , Efficiency = ((followers*100/1000000) * (multipliers*100/20))/100 as Efficiency from users;

# Task 5
alter table users modify column multipliers varchar(20);
