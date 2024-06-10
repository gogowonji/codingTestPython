-- 다른 테이블에 동일한 컬럼명이 있을 수 있다.
-- 어떤 값을 원하는지 문제를 꼼꼼히 보기
-- date_format 주의
-- 정렬 우선순위 쉼표로 표시 가능
SELECT b.TITLE, b.BOARD_ID, r.REPLY_ID, 
    r.WRITER_ID, r.CONTENTS, date_format(r.CREATED_DATE,'%Y-%m-%d') as CREATED_DATE
from USED_GOODS_BOARD b
inner join USED_GOODS_REPLY r on b.BOARD_ID = r.BOARD_ID
where YEAR(b.CREATED_DATE) = 2022 and MONTH(b.CREATED_DATE) = 10
order by r.CREATED_DATE, b.TITLE;
