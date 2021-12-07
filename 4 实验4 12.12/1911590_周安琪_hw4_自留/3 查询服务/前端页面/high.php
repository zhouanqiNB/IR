<?php

/**
 * Codeing by ZAQ
 */

$this->title = '12社区高级搜索1';
$this->params['breadcrumbs'][] = $this->title;
?>

<!-- Container fluid Starts -->

<center>

    <img src="../assets/img/12clubLogo.png" alt="12clubLogo"style="zoom:29%;">

    <form action="" method="post" name="form1">
        <table width="500" border="0" cellpadding="0" cellspacing="0">
        <tr><td width="500" height="50">标题：<input type="text" name="title" size="65"></td></tr>
        <tr><td width="500" height="50">最近更新：<input type="text" name="updateNum" size="65"></td></tr>
        <tr><td width="500" height="50">更新日期（格式：2021-09-06）：<input type="text" name="date" size="65"></td></tr>
        <tr><td width="500" height="50">字幕组：<input type="text" name="fansub" size="65"></td></tr>
        <tr><td width="500" height="50">标签（可选：动画、漫画等）：<input type="text" name="tag" size="65"></td></tr>
        <tr><td width="500" height="50"><input type="submit" name="submit" value="Search" size="55"></td></tr>
        </table>
    </form>

    <?php
        error_reporting(0);
        // 我希望获取到keyword之后拿到es里面去查一下。
        if( $_POST["submit"] == "Search"){//如果按的是这个按钮

            // $params = array(); #传递给python脚本的入口参数  

            $title = $_POST['title'];  
            if($title==""){
                $title="empty";
            } 
            $updateNum = $_POST['updateNum'];   
            if($updateNum==""){
                $updateNum="empty";
            }
            $date = $_POST['date'];   
            if($date==""){
                $date="empty";
            } 
            $fansub = $_POST['fansub'];   
            if($fansub==""){
                $fansub="empty";
            } 
            $tag = $_POST['tag'];   
            if($tag==""){
                $tag="empty";
            }

            $path="python3 /mnt/c/Users/16834/Desktop/NKUSearch/test2.py "; //需要注意的是：末尾要加一个空格
             
            @passthru($path.$title." ".$updateNum." ".$date." ".$fansub." ".$tag);//等同于命令`python python.py 参数`，并接收打印出来的信息 
            
            // 剩下的看python的好了。

        }

    ?>

</center>