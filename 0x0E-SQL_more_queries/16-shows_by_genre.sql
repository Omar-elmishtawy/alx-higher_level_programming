-- mklsda
SELECT t.`title`, g.`name`
  FROM `tv_shows` AS tv
       LEFT JOIN `tv_show_genres` AS gen
       ON tv.`id` = gen.`show_id`
       LEFT JOIN `tv_genres` AS tvg
       ON gen.`genre_id` = tvg.`id`
 ORDER BY tv.`title`, tvg.`name`;
