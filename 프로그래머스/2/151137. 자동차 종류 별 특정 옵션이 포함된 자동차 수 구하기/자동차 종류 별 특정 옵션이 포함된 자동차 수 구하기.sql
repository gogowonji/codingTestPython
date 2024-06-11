-- 한 컬럼에 여러 값이 있고, 그 값을 추출해내야 할 때
-- LIKE 옵션으로 사용할 수 있음
SELECT CAR_TYPE, COUNT(CAR_TYPE) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%통풍시트%'
    or OPTIONS LIKE '%열선시트%'
    or OPTIONS LIKE '%가죽시트%'
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE;
