<?php
/**
 * Team: 写的都对, NKU
 * Coding by ZhouAnQi 1911590, 20211127
 * 这是总体的模板
 */

/* @var $this \yii\web\View */
/* @var $content string */

use frontend\assets\AppAsset;
use yii\helpers\Html;
use yii\bootstrap\Nav;
use yii\bootstrap\NavBar;
use yii\widgets\Breadcrumbs;
use common\widgets\Alert;



AppAsset::register($this);
?>
<?php $this->beginPage() ?>



<!DOCTYPE html>
<html lang="en">
	<head>
		<!-- <meta charset="UTF-8" /> -->
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="shortcut icon" href="../assets/img/fav.png">
		<title><?= Html::encode($this->title) ?></title>
		
		<!-- Bootstrap CSS -->
		<link href="../assets/css/bootstrap.min.css" rel="stylesheet" media="screen" />

		<!-- Main CSS -->
		<link href="../assets/css/main.css" rel="stylesheet" media="screen" />

		<!-- Ion Icons -->
		<link href="../assets/fonts/icomoon/icomoon.css" rel="stylesheet" />
		
		<!-- C3 CSS -->
		<link href="../assets/css/c3/c3.css" rel="stylesheet" />

		<!-- NVD3 CSS -->
		<link href="../assets/css/nvd3/nv.d3.css" rel="stylesheet" />

		<!-- Horizontal bar CSS -->
		<link href="../assets/css/horizontal-bar/chart.css" rel="stylesheet" />

		<!-- Calendar Heatmap CSS -->
		<link href="../assets/css/heatmap/cal-heatmap.css" rel="stylesheet" />

		<!-- Circliful CSS -->
		<link rel="stylesheet" href="../assets/css/circliful/circliful.css" />

		<!-- OdoMeter CSS -->
		<link rel="stylesheet" href="../assets/css/odometer.css" />

		<!-- HTML5 shiv and Respond.js IE8 support of HTML5 elements and media queries -->
		<!--[if lt IE 9]>
			<script src="js/html5shiv.js"></script>
			<script src="js/respond.min.js"></script>
		<![endif]-->

		<!-- echarts -->
		<script src="https://cdn.staticfile.org/echarts/4.3.0/echarts.min.js"></script>
		


	</head>

	<body>
	<?php $this->beginBody() ?>

		<!-- Loading starts -->
		<div class="loading-wrapper">
			<div class="loading">
				<h5>Loading...</h5>
				<span></span>
				<span></span>
				<span></span>
				<span></span>
				<span></span>
				<span></span>
			</div>
		</div>
		<!-- Loading ends -->

		<!-- Header starts -->
		<header>

			<!-- Logo starts -->
<!-- 			<a href="?r=site/index" class="logo">
				<img src="../assets/img/logo.png" alt="Olympics Logo" />
			</a>  -->
			<!-- Logo ends -->



		</header> 
		<!-- Header ends -->

		<!-- Left sidebar start -->
		<div class="vertical-nav vertical-nav-sm">

			<!-- Collapse menu starts -->
			<button class="collapse-menu">
				<i class="icon-menu2"></i>
			</button>
			<!-- Collapse menu ends -->

			<!-- Current user starts -->
<!-- 			<div class="user-details clearfix">
				<a href="" class="user-img"></a>
			</div> -->
			<!-- Current user ends -->

			<!-- Sidebar menu start -->
			<ul class="menu clearfix">

				<!-- 12club 开始 -->
				<li>
					<a href="?r=site/index">
						<i class="icon-award4"></i>
						<span class="menu-item">12社区资源搜索</span>
						<!-- <span class="down-arrow"></span> -->
					</a>
				</li>
				<li>
					<a href="?r=site/high">
						<i class="icon-award4"></i>
						<span class="menu-item">12社区高级搜索1</span>
						<!-- <span class="down-arrow"></span> -->
					</a>
				</li>
				<li>
					<a href="?r=site/high2">
						<i class="icon-award4"></i>
						<span class="menu-item">12社区高级搜索2</span>
						<!-- <span class="down-arrow"></span> -->
					</a>
				</li>
				<li>
					<a href="?r=site/history">
						<i class="icon-award4"></i>
						<span class="menu-item">我的历史查询</span>
						<!-- <span class="down-arrow"></span> -->
					</a>
				</li>
				<!-- 12club 结束 -->

			<!-- Sidebar menu snd -->
		</div>
		<!-- Left sidebar end -->

		<!-- Dashboard Wrapper Start -->
		<div class="dashboard-wrapper">

			<?= $content ?>
		
		</div>
		<!-- Dashboard Wrapper End -->

		<!-- Footer Start -->
		<footer>
			Copyright <a href="https://github.com/NKUZAQ/">ZAQ</a> <span>2021.12</span>
		</footer>
		<!-- Footer end -->

		<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
		<script src="../assets/js/jquery.js"></script>

		<!-- Include all compiled plugins (below), or include individual files as needed -->
		<script src="../assets/js/bootstrap.min.js"></script>

		<!-- Sparkline Graphs -->
		<!-- <script src="js/sparkline/sparkline.js"></script> -->
		<script src="../assets/js/sparkline/retina.js"></script>
		<script src="../assets/js/sparkline/custom-sparkline.js"></script>
		
		<!-- jquery ScrollUp JS -->
		<script src="../assets/js/scrollup/jquery.scrollUp.js"></script>

		<!-- D3 JS -->
		<script src="../assets/js/d3/d3.v3.min.js"></script>
		<script src="../assets/js/d3/d3.powergauge.js"></script>

		<!-- C3 Graphs -->
		<script src="../assets/js/c3/c3.min.js"></script>
		<script src="../assets/js/c3/c3.custom.js"></script>

		<!-- NVD3 JS -->
		<script src="../assets/js/nvd3/nv.d3.js"></script>
		<script src="../assets/js/nvd3/nv.d3.custom.boxPlotChart.js"></script>

		<!-- Horizontal Bar JS -->
		<script src="../assets/js/horizontal-bar/horizBarChart.min.js"></script>
		<script src="../assets/js/horizontal-bar/horizBarCustom.js"></script>

		<!-- Gauge Meter JS -->
		<script src="../assets/js/gaugemeter/gaugeMeter-2.0.0.min.js"></script>
		<script src="../assets/js/gaugemeter/gaugemeter.custom.js"></script>

		<!-- Calendar Heatmap JS -->
		<script src="../assets/js/heatmap/cal-heatmap.min.js"></script>
		<script src="../assets/js/heatmap/cal-heatmap.custom.js"></script>

		<!-- Odometer JS -->
		<script src="../assets/js/odometer/odometer.min.js"></script>
		<script src="../assets/js/odometer/custom-odometer.js"></script>

		<!-- Peity JS -->
		<script src="../assets/js/peity/peity.min.js"></script>
		<script src="../assets/js/peity/custom-peity.js"></script>

		<!-- Circliful js -->
		<script src="../assets/js/circliful/circliful.min.js"></script>
		<script src="../assets/js/circliful/circliful.custom.js"></script>		

		<!-- Custom JS -->
		<script src="../assets/js/custom.js"></script>


	<?php $this->endBody() ?>

	</body>
</html>


<?php $this->endPage() ?>
