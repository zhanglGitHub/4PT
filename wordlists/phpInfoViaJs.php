<html>
<title>Chilico PoC for PHPinfo via JS</title>
<body>
The PHP info()

<?php
phpinfo();
?>
<script>
    alert(document.getElementsByTagName('body')[0].innerHTML);
</script>

</body>
</html>

