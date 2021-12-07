<?php

/**
 * Codeing by ZAQ
 */

$this->title = '我的历史记录';
$this->params['breadcrumbs'][] = $this->title;


error_reporting(0);

$path="python3 /mnt/c/Users/16834/Desktop/NKUSearch/readHistory.py "; 
// echo $path.$must." ".$not;
@passthru($path);//等同于命令`python 





?>