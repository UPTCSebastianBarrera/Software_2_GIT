<?php

$host='localhost';
$bd='ChatbotQA';
$user='postgres';
$pass='1234';

$conexion=pg_connect("host=$host dbname=$bd user=$user password=$pass");

if(isset($_POST['guardar']))
{

  $pregunta = $_POST['pregunta'];

  foreach ($name as $index => $names) {
   
    echo $names;
  }

}






?>