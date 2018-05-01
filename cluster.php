<?php
    $fp = fopen('browser_request.csv', 'w');
    $coordinates = $_GET['coordinates'];
    $coordinates = json_decode($coordinates);
    foreach ($coordinates as $key => $value) {
        $data = (array)$value;
        fputcsv($fp, $data);
    }
    fclose($fp);
    $output = shell_exec('python DBSCAN.py');
    var_dump($output);
    // $fp = fopen('labels.csv',r);
    // while(!FEOF($fp)){
    //     print_r(fgetcsv($fp));
    // }
    // fclose($fp);
?>
