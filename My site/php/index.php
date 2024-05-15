<?php
		include "head.php";
		include "header.php";


		switch ($s)
		{
			case 1:
				include "content/home.php";
				break;
			case 2:
				include "content/catalog.php";
				break;
			case 3:
				include "content/projects.php";
				break;
			case 4:
				include "content/about.php";
				break;
			default: include "content/home.php";
				break;
		}

		include "footer.php";
?>