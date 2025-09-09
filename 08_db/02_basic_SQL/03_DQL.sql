USE world;

-- SELECT 활용 1
-- 테이블 country 에서 Name 필드의 모든 데이터를 조회
SELECT 
  Name
FROM 
  country;

-- SELECT 활용 2
-- 테이블 country 에서 Code, Name 필드의 모든 데이터를 조회
SELECT 
  Code, Name 
FROM 
  country;


-- SELECT 활용 3
-- 테이블 country 에서 모든 필드 데이터를 조회
SELECT *
FROM country;

-- SELECT 활용 4
-- 테이블 country 에서 Name 필드의 모든 데이터를 조회
-- (단, 조회 시 Name 이 아닌 ‘국가’로 출력 될 수 있도록 변경)
SELECT 
  Name AS '국가'
FROM 
  country;

-- SELECT 활용 5
-- 테이블 country에서 Name, Population 필드의 모든 데이터 조회
-- (단, Population 필드는 1000 으로 나눠 k 단위 값으로 출력)
SELECT
  Name,
  Population / 1000 AS '인구 (k)'
FROM
  country;

-------------------------------------------
-- Filtering Data

-- Distinct 활용
-- 테이블 country에서 Continent 필드의 데이터를 중복없이 조회
SELECT 
  DISTINCT Continent
FROM 
  country;

-- WHERE 활용 1
-- 테이블 country 에서 Region 필드 값이 ‘Eastern Asia’인 데이터의 Name, Population 조회
SELECT 
  Name, Population
FROM 
  country
WHERE Region = 'Eastern Asia';


-- WHERE 활용 2
-- 테이블 country 에서 IndepYear 필드 값이 Null이 아닌 
-- 데이터의 Name, Region, Population, IndepYear 조회
SELECT 
  Name, Region, Population, IndepYear
FROM 
  country
WHERE
  IndepYear IS NOT NULL;


-- WHERE 활용 3
-- 테이블 country 에서 Population 필드 값이 천 만 이상이고 
-- LifeExpectancy 필드가 78 이상인 데이터의 
-- Name, Region, LifeExpectancy 조회
SELECT
  Name, Region, LifeExpectancy
FROM 
  country
WHERE
  Population >= 10000000 
  AND LifeExpectancy >= 78;


