-- 코드를 작성해주세요
-- 부모 ID를 가진 놈들이 자식
-- parent_id이 없는 놈은 부모
SELECT ID, IFNULL((SELECT COUNT(*)
                  FROM ECOLI_DATA
                  GROUP BY PARENT_ID
                  HAVING ID = PARENT_ID)
                  ,0) AS CHILD_COUNT
FROM ECOLI_DATA
ORDER BY ID;
