<?php

function udate($format = 'u', $utimestamp = null) {
        if (is_null($utimestamp))
            $utimestamp = microtime(true);

        $timestamp = floor($utimestamp);
        $milliseconds = round(($utimestamp - $timestamp) * 1000000);

        return date(preg_replace('`(?<!\\\\)u`', $milliseconds, $format), $timestamp);
    }

// Required for output buffering.
header('Content-type:text/html;charset=utf-8');
//Set size of buffer window to minimum value
echo str_repeat(' ',1024*64);

$json_datatable_str = '{
  "cols":[
    {"id":"","label":"Timestamp","type":"string"},
    {"id":"","label":"Sensor_Data","type":"number"},
  ],
  "rows":[
';

$json_datatable_str2 = '{
  "cols":[
    {"id":"","label":"Timestamp","type":"string"},
    {"id":"","label":"Sensor_Data","type":"number"},
  ],
  "rows":[
';

$json_datatable_str3 = '{
  "cols":[
    {"id":"","label":"Timestamp","type":"string"},
    {"id":"","label":"Sensor_Data","type":"number"},
  ],
  "rows":[
';
file_put_contents('new.json',$json_datatable_str2 );
file_put_contents('new1.json',$json_datatable_str2 );
file_put_contents('new3.json',$json_datatable_str2 );
file_put_contents('new2.json',$json_datatable_str2 );


$json_str_terminator = ']}';
//To increase execution time of script
set_time_limit(100000);
ob_end_flush();
ob_implicit_flush(true);

//Connection Establishment Phase with MySQL
$user = 'root' ; 			//username
$pass = '' ;				//password
$db = 'training' ;			//database

//Start output Buffering
ob_start();
//Connect or fail
$db = new mysqli('localhost' , $user , $pass , $db) or die('Connection Failed');

//Database  
//Query to extract sensor details. Sampling frequency used in further steps
$sql_query = "select SENSOR_ID,ORIGINAL_WAVE,SAMPLING_FREQUENCY from sensor";
$result = $db->query($sql_query);

$no_of_sensors = $result->num_rows;

if($result->num_rows >0)		//Iterate over all tuples(for multiple sensors)
{
	while($row = $result->fetch_assoc())
	{
		echo "id : " . $row["SENSOR_ID"].  "<br>" ."original wave function : " .$row["ORIGINAL_WAVE"]. "<br>" ."SAMPLING FREQUENCY :" .$row["SAMPLING_FREQUENCY"] ."<br>" ;
		$s_rate = $row["SAMPLING_FREQUENCY"];
		flush();
		ob_flush();
	}
}		


//DateTime variable to store Time till which values have been received for analytics 
$last_received_timestamp = new DateTime();
$last_received_timestamp->setTimestamp(1171502725);
//echo $last_received_timestamp->format('U = Y-m-d H:i:s')."\n";
echo $s_rate; 		//Sampling Frequency
$last_sensor_id = 'S01';
ob_flush();
$i = 0;


//while(1) for actual case . It receives values from the database in discrete time intervals.
//Hence analytics can be done on a part of the data.
$sensor_data = Array(Array());
$sensor_top = Array();
for($iterator = 0; $iterator < $no_of_sensors ; $iterator++)
{
	//echo $iterator."<br>";
	$sensor_top[$iterator] = 0;
	
}
$flagg = 0;
$flagg2 = 0;
$flagg3 = 0;
$kkk = '2011-05-05 05:11:56.786';
$count_elements_in_graph = 0;
while(1)
{
	//echo $last_received_timestamp->format('Y-m-d H:i:s');
	$sql_get_data = "select SENSOR_ID,RECEIVE_TIME,DATA_RECEIVED from SENSOR_DATA where RECEIVE_TIME>'".$kkk."' order by RECEIVE_TIME";
	//echo $sql_get_data;
	
	$result = $db->query($sql_get_data);
	//echo $no_of_sensors;
	$json = array();
	if($result->num_rows >0)
	{
		while($row = $result->fetch_assoc())
		{
			$last_received_timestamp = new DateTime();
			$last_sensor_id = $row["SENSOR_ID"];
			$kkk = $row["RECEIVE_TIME"];
			//echo udate('Y-m-d H:i:s.u',$last_received_timestamp->format('U'));
			$last_received_timestamp->createFromFormat('Y-m-d H:i:s.u', $kkk);
			//echo $kkk.'   '.$last_received_timestamp->format('Y-m-d H:i:s.u');
			//echo "Using DateTime: ".$last_received_timestamp->format("Y-m-d H:i:s.u");
			//$last_received_timestamp->setTimestamp(DateTime::createFromFormat('Y-m-d H:i:s.u', $row["RECEIVE_TIME"]));
			//echo udate('Y-m-d H:i:s.u',$last_received_timestamp["RECEIVE_TIME"]->format('U'));
			echo "id : " . $row["SENSOR_ID"].  "  " ."Timestamp : " .$row["RECEIVE_TIME"]. "   " ."Data received " .$row["DATA_RECEIVED"] ."<br>" ;
			
			
			//$last_received_timestamp = udate('Y-m-d H:i:s.u',$last_received_timestamp->format('U'));
			$json['Sensor_Data'] = $row["DATA_RECEIVED"];
			$json['Timestamp'] = $last_received_timestamp->format("Y-m-d H:i:s.u");
			$data[] =$json;
			
			//print udate('Y-m-d H:i:s.u',$last_received_timestamp->format('U'));
					
			
			
			
			switch($row["SENSOR_ID"])
			{
				case "S01" :
					$sensor_data[0][$sensor_top[0]] = $row["DATA_RECEIVED"];
					$sensor_top[0] = $sensor_top[0] + 1 ; 
					
					$file = 'sensor1.txt';
					$current = file_get_contents($file);
					$current = $current.$row["DATA_RECEIVED"]."  ".$row["RECEIVE_TIME"]."\n";
					file_put_contents($file,$current);
					
					if($flagg == 0)
					{
						$json_datatable_entry ='{"c":[{"v":"'.$kkk.'"},{"v":'.$row["DATA_RECEIVED"].'}]} ';
						$flagg = 1;
					}
					else
					{
						$json_datatable_entry =',{"c":[{"v":"'.$kkk.'"},{"v":'.$row["DATA_RECEIVED"].'}]} ';
					}
					$new_json_str = $json_datatable_str.$json_datatable_entry.$json_str_terminator;
					$json_datatable_str = $json_datatable_str.$json_datatable_entry;
					$inp = file_get_contents('new.json');
	
					file_put_contents('new.json',$new_json_str);
					$count_elements_in_graph = $count_elements_in_graph + 1;
				
					break;
					
				case "S02" :
					$sensor_data[1][$sensor_top[1]] = $row["DATA_RECEIVED"];
					$sensor_top[1] = $sensor_top[1] + 1;
					
					$file = 'sensor2.txt';
					$current = file_get_contents($file);
					$current = $current.$row["DATA_RECEIVED"]."  ".$kkk."\n";
					file_put_contents($file,$current);
					
					if($flagg2 == 0)
					{
						$json_datatable_entry2 ='{"c":[{"v":"'.$kkk.'"},{"v":'.$row["DATA_RECEIVED"].'}]} ';
						$flagg2 = 1;
					}
					else
					{
						$json_datatable_entry2 =',{"c":[{"v":"'.$kkk.'"},{"v":'.$row["DATA_RECEIVED"].'}]} ';
					}
					$new_json_str2 = $json_datatable_str2.$json_datatable_entry2.$json_str_terminator;
					$json_datatable_str2= $json_datatable_str2.$json_datatable_entry2;
					$inp = file_get_contents('new2.json');
	
					file_put_contents('new2.json',$new_json_str2);
					
					break;
					
					
				case "S03" :
					$sensor_data[2][$sensor_top[2]] = $row["DATA_RECEIVED"];
					$sensor_top[2] = $sensor_top[2] + 1;
					
					$file = 'sensor3.txt';
					$current = file_get_contents($file);
					$current = $current.$row["DATA_RECEIVED"]."  ".$kkk."\n";
					file_put_contents($file,$current);
					
					if($flagg3 == 0)
					{
						$json_datatable_entry3 ='{"c":[{"v":"'.$kkk.'"},{"v":'.$row["DATA_RECEIVED"].'}]} ';
						$flagg3 = 1;
					}
					else
					{
						$json_datatable_entry3 =',{"c":[{"v":"'.$kkk.'"},{"v":'.$row["DATA_RECEIVED"].'}]} ';
					}
					$new_json_str3 = $json_datatable_str3.$json_datatable_entry3.$json_str_terminator;
					$json_datatable_str3= $json_datatable_str3.$json_datatable_entry3;
					$inp = file_get_contents('new3.json');
	
					file_put_contents('new3.json',$new_json_str3);
					
					break;
					
				default:
			
			}
			
			//echo $last_received_timestamp->format('Y-m-d H:i:s');
			ob_flush();
			flush();
		}
	}
	else
	{
		echo "Sleeping"."<br>";
		sleep(2.0);
		flush();
		ob_flush();
	}
	$i++;
	//echo $last_received_timestamp->format('Y-m-d H:i:s');
	
}
print json_encode($data);
for($iterator = 0; $iterator < $no_of_sensors ; $iterator++)
{
	echo "Sensor  ".($iterator+1)." readings  <br>";
	for($j_iterator = 0; $j_iterator < $sensor_top[$iterator] ; $j_iterator++)
		echo $sensor_data[$iterator][$j_iterator]."  ";
	echo "<br>";
}

echo '<script type="text/javascript">','drawChart();','</script>' ;
$db->close();
echo "This runs" ; 
ob_flush();
ob_end_flush();
?>

