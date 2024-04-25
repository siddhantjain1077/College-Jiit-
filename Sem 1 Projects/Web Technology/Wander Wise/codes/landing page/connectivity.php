<?php

// Database connection parameters
$servername = "localhost";
$username = "user";
$password = "minaxi16";
$dbname = "user";

// Create a connection
$conn = new mysqli($servername, $username, $password, $dbname,"3306");

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Create the users table if it doesn't exist
$tableSql = "CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20),
    address VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL
)";

if ($conn->query($tableSql) === TRUE) {
    echo "Table created or exists.";
} else {
    echo "Error creating table: " . $conn->error;
}

// Get form data
$name = isset($_POST['name']) ? $conn->real_escape_string($_POST['name']) : '';
$phone_number = isset($_POST['phone_number']) ? $conn->real_escape_string($_POST['phone_number']) : '';
$address = isset($_POST['address']) ? $conn->real_escape_string($_POST['address']) : '';
$email = isset($_POST['email']) ? $conn->real_escape_string($_POST['email']) : '';
$username = isset($_POST['username']) ? $conn->real_escape_string($_POST['username']) : '';
$password = isset($_POST['password']) ? $conn->real_escape_string($_POST['password']) : '';


// Hash the password (for security)
$hashed_password = password_hash($password, PASSWORD_DEFAULT);

// Prepare and execute the SQL statement to insert data into the database
$insertSql = "INSERT INTO users (name, phone_number, address, email, username, password) VALUES (?, ?, ?, ?, ?, ?)";

$stmt = $conn->prepare($insertSql);
$stmt->bind_param("ssssss", $name, $phone_number, $address, $email, $username, $hashed_password);

if ($stmt->execute()) {
    echo "New record created successfully";
} else {
    echo "Error: " . $stmt->error;
}

// Close the database connection
$stmt->close();
$conn->close();

?>
