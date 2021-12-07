<?php

/**
 * Codeing by ZAQ
 */

$this->title = '12社区资源搜索';
$this->params['breadcrumbs'][] = $this->title;
?>

<!-- Container fluid Starts -->

<center>

    <img src="../assets/img/12clubLogo.png" alt="12clubLogo"style="zoom:29%;">

    <form action="" method="post" name="form1">
        <table width="500" border="0" cellpadding="0" cellspacing="0">
        <tr>
            <td width="500" height="50">
                <input type="text" name="keyword" size="55">
                <input type="submit" name="submit" value="Search">
            </td>
        </tr>
        </table>
    </form>
    <?php
        error_reporting(0);
        // 我希望获取到keyword之后拿到es里面去查一下。
        if( $_POST["submit"] == "Search"){//如果按的是这个按钮
         // 使用 echo 語句輸出使用 $_POST[] 方法獲取的使用者名稱和密碼
            // echo "keyword:". $_POST['keyword'];



            $params = $_POST['keyword']; #传递给python脚本的入口参数  
            $path="python3 /mnt/c/Users/16834/Desktop/NKUSearch/test.py "; //需要注意的是：末尾要加一个空格
             
             
            passthru($path.$params);//等同于命令`python python.py 参数`，并接收打印出来的信息 

            // 剩下的看python的好了。

        }

    ?>

</center>


