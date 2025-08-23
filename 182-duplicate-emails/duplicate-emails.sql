# Write your MySQL query statement below
Select
    p.email
From
    Person P
Group BY
    p.email
Having
    Count(p.email)>1