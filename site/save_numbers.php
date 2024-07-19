<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);
    if (isset($data['numbers'])) {
        $numbers = implode(", ", $data['numbers']);
        file_put_contents('queue.txt', $numbers . PHP_EOL, FILE_APPEND);
        http_response_code(200);
    } else {
        http_response_code(400);
    }
} else {
    http_response_code(405);
}
?>
