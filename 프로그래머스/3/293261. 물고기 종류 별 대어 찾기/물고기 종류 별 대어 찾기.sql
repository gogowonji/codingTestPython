-- 서브 쿼리, 다중값 IN 좋다! 배워가기
SELECT f.ID, fn.FISH_NAME, f.LENGTH
FROM FISH_INFO f
INNER JOIN FISH_NAME_INFO fn ON f.FISH_TYPE = fn.FISH_TYPE
WHERE (f.FISH_TYPE, f.LENGTH) IN (SELECT FISH_TYPE, MAX(LENGTH)
                            FROM FISH_INFO
                            GROUP BY FISH_TYPE)
ORDER BY f.ID;
-- ORDER BY 1; -- 해도 됨
