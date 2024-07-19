<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);
    if (isset($data['numbers'])) {
        $numbers = $data['numbers'];
        $valid = true;
        foreach ($numbers as $number) {
            if (!preg_match('/^[a-zA-Z_][a-zA-Z0-9_-]*$/', $number)) {
                $valid = false;
                break;
            }
        }
        if ($valid) {
            $numbers_str = implode(", ", $numbers);
            file_put_contents('queue.txt', $numbers_str . PHP_EOL, FILE_APPEND);
            http_response_code(200);
        } else {
            http_response_code(400);
            echo json_encode(["error" => "Invalid number format"]);
        }
    } else {
        http_response_code(400);
        echo json_encode(["error" => "Invalid data"]);
    }
} else {
    http_response_code(405);
}
?>
