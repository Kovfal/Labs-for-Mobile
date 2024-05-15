<?php

if(isset($_GET["s"])) $s=$_GET["s"];
else $s=1;


echo '
<body>
		<header class="header">
			<div class="container">

				<nav class="nav">
					<a class="logo" href=index.php?s=1>LOGO COMPANY</a>
					<a class="nav-item" href=index.php?s=2>Каталог</a>
					<a class="nav-item" href=index.php?s=3>Проекты</a>
					<a class="nav-item" href=index.php?s=4>О компании</a>

					<form action="" method="get" id="searchform">
						<input type="text" placeholder="Поиск...">
						<button type="submit"><i class="fa fa-search"></i></button>
					</form>
				</nav>

			</div>
		</header>
';

echo '
	<main>
	';

?>