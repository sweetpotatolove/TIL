-- Operator

-- BETWEEN Operator example
-- 테이블 country 에서 Poputation 필드 값이 백만이상 오백만이하이고 
-- GNPOld가 GNP 보다 큰 데이터의 
-- Name, Region, Population 그리고 GNPOld와 GNP 차이를 
-- GNP diff로 작성하여 조회
SELECT
  Name, Region, Population, 
  GNP - GNPOld AS 'GNP Diff' 
FROM 
  country
WHERE
  Population BETWEEN 1000000 AND 5000000
  -- Population >= 1000000 AND Population <= 5000000
  AND GNP < GNPOld;


-- IN Operator example
-- 테이블 country 에서 Continent 필드 값이 
-- ‘North America’ 또는 ‘Asia’ 인 데이터의 Code, Name, Continent 조회
SELECT
  Code, Name, Continent
FROM
  country
WHERE
  Continent IN ('North America', 'Asia');
-- WHERE
--   Continent = 'North America' OR Continent = 'Asia';


-- Like Operator example 1
-- 테이블 country에서 Name 필드 값이 ‘South’으로 시작하는 데이터의
-- Name, Region, Population, GNP 조회
SELECT 
  Name, Region, Population, GNP
FROM 
  country
WHERE
  Name LIKE 'South%';


-- Like Operator example 2
-- 테이블 country에서 Name 필드 값이 ‘South’으로 시작하고, 
-- 공백을 포함하여 6자리를 가지는 데이터의
-- Name, Region, Population, GNP 조회
SELECT 
  Name, Region, Population, GNP 
FROM 
  country
WHERE
  Name LIKE 'South______';


-- NULL 값은 = 연산자를 이용하여 비교하지 않음
  -- NULL은 어떤 값과도 같지 않기 때문에
-- SELECT 
--   Name, GNPOld, IndepYear
-- FROM 
--   country
-- WHERE
--   GNPOld = NULL
--   AND IndepYear != NULL;


-- IS Operator example
SELECT 
  Name, GNPOld, IndepYear
FROM 
  country
WHERE
  GNPOld IS NULL
  AND IndepYear IS NOT NULL;

-- Operator 우선 순위 example
-- Ver. Wrong
-- AND 연산자의 우선순위가 OR보다 높으므로,
-- LifeExpectancy가 75보다 높은 경우도 조회된다.
SELECT 
  Name, IndepYear, LifeExpectancy
FROM 
  country
WHERE
  IndepYear = 1901 OR IndepYear = 1981 
  AND LifeExpectancy <= 75;

-- Ver. Wrong 2
-- 현재는 정상적으로 조회되는 듯 보일 수 있으나, 데이터에 따라 달라질 수 있다.
SELECT 
  Name, IndepYear, LifeExpectancy
FROM 
  country
WHERE
  IndepYear = 1981 OR IndepYear = 1901 
  AND LifeExpectancy <= 75;

-- Ver. Good
SELECT 
  Name, IndepYear, LifeExpectancy
FROM 
  country
WHERE
  (IndepYear = 1901 OR IndepYear = 1981)
  AND LifeExpectancy <= 75;


