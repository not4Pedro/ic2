<?php
	$authenticated=false;
	if(null !== $_POST['verify'] && $_POST['verify']=="Verify")
	{
		$cn = pg_connect("host=localhost port=5432 dbname=ic2 user=postgres password=postgres");
		$username=$_POST['username'];
		$query = "select * from verify($1);";
		$res = pg_query_params($cn,$query,array($username));
		$result = pg_fetch_object($res);
		if($result)
		{
			$authenticated=$result->verify==1;
		}
		if (!$authenticated)
		{
			$output = "Wrong user or pass";
		}
		else
		{
			$output = "Wrong password";
		}
	}
?>
<!DOCTYPE html>
<html>
<head>
	<title>LOGIN</title>
	<link href='https://css.gg/arrow-right-o.css' rel='stylesheet'>
	<link rel="stylesheet" href="./style.css" type="text/css"/>
	<link href='https://css.gg/password.css' rel='stylesheet'>
</head>
<body>
	<div class="container">
			<form method="post">
			<div class="form-input">
				<input type="text" name="username" placeholder="Enter the username"/>	
			</div>
			<div class="form-input">
				<i class="gg-password"></i>
				<input type="password" name="password" placeholder="password"/>
			</div>
			<input type="submit" value="Verify" name="verify" class="btn-login"/>
			</form>
			<p id="error"><?php echo $output ?></p>
	</div>
</body>
</html>
