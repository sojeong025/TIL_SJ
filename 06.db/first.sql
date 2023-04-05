CREATE TABLE contacts (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  email TEXT NOT NULL UNIQUE
);

-- rename a table
ALTER TABLE contacts RENAME TO new_contacts;

-- rename a column
ALTER TABLE new_contacts RENAME COLUMN name TO last_name;

-- add a new column to a table
ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL;
-- cannot add NOT NULL column with default value NULL 오류 발생 > 만들어지지 않음
ALTER TABLE new_contacts
ADD COLUMN address TEXT NOT NULL DEFAULT 'no address';

-- delete a column
ALTER TABLE new_contacts DROP COLUMN address;

-- drop table
DROP TABLE contacts;


CREATE table users(
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

-- select statement (1/2)
-- 특정 테이블에서 데이터를 조회하기 위해 사용
-- 문법 : 1. SELECT 절에서 컬럼 또는 쉼표로 구분된 컬럼 목록을 지정 2. FROM 절(clause)에서 데이터를 가져올 테이블을 지정

SELECT * FROM users;

SELECT DISTINCT first_name, country FROM users
ORDER BY country;



