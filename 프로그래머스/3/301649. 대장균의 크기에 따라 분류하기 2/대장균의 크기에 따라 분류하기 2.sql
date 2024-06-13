-- 정렬 컬럼 갯수로 가져오기....?
-- -> 아니었음
-- NTILE() 구간 나누는 순위 함수로 구하기
-- ID 가져오기 (**주의**)

SELECT L.ID,(CASE
        WHEN L.LEVEL = 1 THEN 'CRITICAL'
        WHEN L.LEVEL = 2 THEN 'HIGH'
        WHEN L.LEVEL = 3 THEN 'MEDIUM'
        ELSE 'LOW'
        END) AS 'COLONY_NAME'
FROM (SELECT ID, NTILE(4) OVER(ORDER BY SIZE_OF_COLONY DESC) AS LEVEL
      FROM ECOLI_DATA) AS L
ORDER BY L.ID;
