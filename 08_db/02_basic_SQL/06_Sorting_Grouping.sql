USE world;

-- Sorting data
-- Order by example 1
SELECT 
  GovernmentForm
FROM 
  country
ORDER BY
  GovernmentForm;

-- Order by example 2
SELECT 
  GovernmentForm
FROM 
  country
ORDER BY
  GovernmentForm DESC;

-- Order by example 3
SELECT 
  GovernmentForm, SurfaceArea
FROM 
  country
ORDER BY
  GovernmentForm DESC, SurfaceArea ASC;

-- Order by example 4
-- NULL 값이 존재할 경우 오름차순 정렬 시 결과에 NULL이 먼저 출력
  -- NULL은 모든 값보다 작기 때문에
SELECT
  Name, IndepYear
FROM
  country
WHERE
  Continent = 'Asia'
ORDER BY 
  IndepYear;

-- Order by example 5
-- NULL 데이터는 마지막에 위치하도록
  -- IS NULL의 결과 NULL인 경우, -> TRUE
  -- IS NULL의 결과 NULL이 아닌 경우, -> FALSE
    -- 1은 0보다 크므로, NULL이 아닌 데이터가 먼저 오게 됨
SELECT
  Name, IndepYear
FROM
  country
WHERE
  Continent = 'Asia'
ORDER BY 
  IndepYear IS NULL, IndepYear;

-- Limit example 1
SELECT 
  IndepYear, Name, Population
FROM 
  country
ORDER BY 
  Population DESC
LIMIT 7;

-- Limit example 2
SELECT 
  IndepYear, Name, Population
FROM 
  country
ORDER BY 
  Population DESC
LIMIT 4, 7;
-- LIMIT 7 OFFSET 4;


-- Aggregate Function​

-- 집계 함수 1
SELECT COUNT(*) FROM country;
SELECT COUNT(IndepYear) FROM country;

-- 집계 함수 2
SELECT SUM(GNP) FROM country WHERE Continent = 'Asia';
SELECT AVG(GNP) FROM country WHERE Continent = 'Asia';

-- 집계 함수 3
SELECT MAX(GNP) FROM country WHERE Continent = 'Asia';
SELECT MIN(GNP) FROM country WHERE Continent = 'Asia';

-- 집계 함수 4
SELECT STDDEV(GNP) FROM country WHERE Continent = 'Asia';
SELECT VARIANCE(GNP) FROM country WHERE Continent = 'Asia';


-- GROUP BY 

-- Group by 예시 1
SELECT
  Continent
FROM
  country
GROUP BY
  Continent;

-- Group by 예시 2
SELECT
  Continent, COUNT(*)
FROM
  country
GROUP BY
  Continent;

-- group by example 1
SELECT
  Continent, 
  ROUND(AVG(GNP), 2) AS avg_gnp
FROM
  country
GROUP BY
  Continent;


-- group by example 2
-- error code
SELECT
  Region,
  COUNT(Region) AS count_reg
FROM
  country
WHERE
  count_reg BETWEEN 15 AND 20 
GROUP BY
  Region
ORDER BY 
  count_reg DESC;

-- correct code
SELECT
  Region,
  COUNT(Region) AS count_reg
FROM
  country
GROUP BY
  Region
HAVING
  count_reg BETWEEN 15 AND 20
ORDER BY 
  count_reg DESC;
