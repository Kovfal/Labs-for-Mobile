<?php

$article_max=17;
$n=5;
$page_max=ceil($article_max/$n);


echo '			<div class="container">'


for($i=1+$page; $i<=$n+$page; $i++)
{
	echo '
					<section>
						<article>
							<header class="postHeader">
								<h1>Название поста №'.i.'</h1>
							</header>
							<div class="text">
								Lorem ipsum dolor sit amet, consectetur adipiscing elit.
								Ut venenatis rutrum erat et sodales.
								Etiam quis sapien in orci molestie gravida id at magna.
							</div>
							<footer class="postFooter">
								<h3>author: NNN</h3>
							</footer>
						</article>
					</section>
	';
	if($i==$article_max) break;
}
for($i=1; $i<=$page_max; $i++)
	echo '<a href=index.php?s=1&page='.($i-1).'>'.$i.'</a> ';
