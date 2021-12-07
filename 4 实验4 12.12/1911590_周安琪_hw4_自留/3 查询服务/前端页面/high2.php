<?php

/**
 * Codeing by ZAQ
 */

$this->title = '12社区高级搜索2';
$this->params['breadcrumbs'][] = $this->title;
?>

<!-- Container fluid Starts -->

<center>

    <img src="../assets/img/12clubLogo.png" alt="12clubLogo"style="zoom:29%;">

    <form action="" method="post" name="form1">
        <table width="500" border="0" cellpadding="0" cellspacing="0">
        <tr><td width="500" height="50">包含(关键词用英文逗号分隔)<input type="text" name="must" size="65"></td></tr>
        <tr><td width="500" height="50">不包含(关键词用英文逗号分隔)<input type="text" name="not" size="65"></td></tr>
        <tr><td width="500" height="50"><input type="submit" name="submit" value="Search" size="55"></td></tr>
        </table>
    </form>

    <?php
        error_reporting(0);
        // 我希望获取到keyword之后拿到es里面去查一下。
        if( $_POST["submit"] == "Search"){//如果按的是这个按钮

            // $params = array(); #传递给python脚本的入口参数  

            $must = $_POST['must'];  
            $not = $_POST['not'];  
            if($must==""){
                echo "不可以为空！";
            } 
            else{
                if($not==""){
                    echo "不可以为空！";
                }else{
                    $path="python3 /mnt/c/Users/16834/Desktop/NKUSearch/test3.py "; //需要注意的是：末尾要加一个空格
                    // echo $path.$must." ".$not;
                    @passthru($path.$must." ".$not);//等同于命令`python 
                }
            }
            
            // 剩下的看python的好了。

        }

    ?>

</center>