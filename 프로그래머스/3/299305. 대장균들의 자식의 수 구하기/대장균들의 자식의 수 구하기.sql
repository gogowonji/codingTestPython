-- 서브 쿼리 사용
-- HAVING (ID = PARENT_ID) 주의 <- 이걸로 ID 별 자식수 가져올 수 있었음
-- 부모 ID를 가진 놈들이 자식
SELECT ID, IFNULL((SELECT COUNT(*)
                  FROM ECOLI_DATA
                  GROUP BY PARENT_ID
                  HAVING ID = PARENT_ID)
                  ,0) AS CHILD_COUNT
FROM ECOLI_DATA
ORDER BY ID;
