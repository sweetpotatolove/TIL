-- Built-in Function
-- 문자형 함수
-- CONCAT
SELECT CONCAT('FirstName', '_', 'LastName');

-- TRIM
SELECT TRIM('   PHONE   ');
SELECT TRIM('-' FROM '---TITLE---');
SELECT TRIM(LEADING '-' FROM '---TITLE---');
SELECT TRIM(TRAILING '-' FROM '---TITLE---');

-- REPLACE
SELECT REPLACE('$10000', '$', '￦');

-- LOCATE
SELECT LOCATE('path', 'www.web-path-site.com/path/');
SELECT LOCATE('path', 'www.web-path-site.com/path/', 10);

-- 숫자형 함수
-- ABS 함수
SELECT ABS(-12);
-- MOD 함수 (나머지 구하기)
SELECT MOD(10, 7);
SELECT 10%7;   -- MOD와 동일함

-- POW 함수 (제곱근 구하기)
SELECT POW(2, 6);   -- 단축어
SELECT POWER(2, 6); -- POW와 동일함 

-- CEIL 함수
SELECT CEIL(3.7);
SELECT CEIL(3.3);
-- FLOOR 함수
SELECT FLOOR(3.7);
SELECT FLOOR(3.2);
-- ROUND 함수
SELECT ROUND(3.7);
SELECT ROUND(3.2);

-- 날짜형 함수
-- 현재 날짜
SELECT CURDATE();
-- 현재 시간
SELECT CURTIME();
-- 현재 날짜 및 시간
SELECT NOW();
-- 시간 포멧 설정하기
SELECT DATE_FORMAT
('2024-08-23 13:35:20', '%b-%d (%a) %r');

-- NULL 관련 함수
-- IFNULL 함수
SELECT IFNULL(NULL, 'expr1 is NULL');
SELECT IFNULL('expr1', 'expr1 is NULL');

-- 데이터베이스 변경
USE world;

-- IFNULL 함수 example
SELECT 
  Name,
  -- IndepYear,  
  IFNULL(IndepYear, 'no_data') 
FROM 
  country
WHERE 
  Continent = 'North America'; 

-- NULLIF 함수
-- NULL과의 비교에서 유용하게 사용된다.
SELECT NULLIF('expr1', 'expr1');
SELECT NULLIF('expr1', 'expr2');


-- NULLIF 함수 example
-- 모든 국가의 정보 중 인구가 0인 경우 NULL 로 표시되도록 조회
SELECT 
  Name, 
  -- Population,
  NULLIF(Population, 0)
FROM country;

-- NULLIF 함수 example2
-- 모든 국가의 정보 중 독립 연도가 NULL인 경우 NULL로 표시되도록 조회
SELECT NULLIF(IndepYear, NULL) FROM country;

-- COALESCE 함수
SELECT COALESCE('expr1', 'expr2', NULL);
SELECT COALESCE(NULL, 'expr2', NULL);
SELECT COALESCE(NULL, NULL, NULL);

-- COALESCE 함수 예시
-- Africa의 기대 수명이 70 미만인 국가의 GNP 정보를 조회
-- GNP가 0이면 GNPOld 값을 사용하고, GNPOld도 NULL인 경우 'No data'를 표시
SELECT
  -- Name, GNP, GNPOld,
  Name,
  COALESCE(NULLIF(GNP, 0), GNPOld, 'No data') AS gnp_data
FROM country
WHERE
  Continent = 'Africa'
  AND LifeExpectancy < 70;

