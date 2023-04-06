-- users table 생성
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);


-- users 테이블의 전체 행 수 조회하기
SELECT COUNT(*) FROM users;

-- 전체 유저의 평균 balance 조회하기
SELECT AVG(balance) FROM users;

-- 전체 유저의 지역 조회
SELECT DISTINCT country FROM users;

-- 전라북도의 평균
SELECT country, AVG(balance) FROM users 
WHERE country='전라북도';

-- 나이가 30살 이상인 사람들의 평균 나이
SELECT AVG(age) FROM users
WHERE age>= 30;

-- 각 지역별로 몇 명씩 살고 있는지 조회
SELECT country, COUNT(*) FROM users GROUP BY country
ORDER BY COUNT(*) DESC;

-- 각 성씨가 몇 명씩 있는지 조회
SELECT last_name, COUNT(*) FROM users
GROUP BY last_name;

-- AS 키워드 사용해 컬럼명 임시로 변경하여 조회 가능
-- * 원본 테이블이 변경되는건 아님

--Change data
CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);

-- 새 행을 테이블에 삽입
INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 23, '서울');

INSERT INTO classmates
VALUES
    ('김철수', 30, '경기'),
    ('이영미', 31, '강원'),
    ('박진성', 26, '전라'),
    ('최지수', 12, '충청'),
    ('정요한', 28, '경상');

-- 테이블 업데이트
-- 2번 데이터의 이름을 '김철수한무두루미', 주소를 '제주도'로 수정
UPDATE classmates
SET name ='김철수한무두루미',
    address = '제주도'
WHERE rowid = 2;

-- 테이블에서 행 삭제
-- 5번 데이터 삭제하기
DELETE FROM classmates
WHERE rowid = 5;

-- 삭제된 것 확인
SELECT rowid, * FROM classmates;

-- 이름에 영이 포함되는 데이터 삭제하기
DELETE FROM classmates 
WHERE name LIKE '%영%';

-- 테이블의 모든 데이터 삭제하기
DELETE FROM classmates;

SELECT TOP 3 * FROM classmates;
SELECT * FROM classmates
LIMIT 3;


SELECT first_name, country FROM users
WHERE country LIKE '%[남북]%';

INSERT INTO users (first_name, age, country)
VALUES ('소정', 26, '경상남도'); 


