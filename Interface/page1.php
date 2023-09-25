<?php

$host='localhost';
$bd='ChatbotQA';
$user='postgres';
$pass='1234';

$conexion=pg_connect("host=$host dbname=$bd user=$user password=$pass");

$query=("INSERT INTO QAs(id,QAs)
	VALUES('$_REQUEST[id]','$_REQUEST[QAs]')");

$consulta=pg_query($conexion,$query);
pg_close();
echo 'Se agrego la pregunta';


?>