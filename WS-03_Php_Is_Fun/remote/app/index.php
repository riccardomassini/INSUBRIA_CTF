<?php

    if(isset($_GET["source"])){
        highlight_file(__FILE__); 
        die();
    }

    session_start();

    class User{
        public $username;

        public function __construct($username) {
            $this->username = $username;
        }
    }

    function containsForbiddenSubstring(string $username, array $forbidden){
        foreach ($forbidden as $substr) {
            if (str_contains($username, $substr)) {
                return true;
            }
        }
        return false;
    }

    $command = False;

    if (isset($_POST["register"])) {
        $username = htmlentities($_POST["username"]);
        $user = new User($username);
        setcookie("user", base64_encode(serialize($user)), time() + 3600, "/");
        header("Location: " . $_SERVER["PHP_SELF"]);
    }

    if (isset($_COOKIE["user"])) {
        $data = base64_decode($_COOKIE["user"]);
        $user = unserialize($data);

        $blacklist = ["flag", "nc", "curl", "cat", "wget", "txt", "eval", "more", "less", "bash", "sh", "php", "system", "exec", "shell", "file"];
        
        if ($user instanceof User && !containsForbiddenSubstring($user->username, $blacklist)) {
            $command = "echo 'Welcome, {$user->username}'";
        }
    }
?>

<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
</head>
<body style="font-family: Arial, sans-serif; background-color: #f4f4f4; text-align: center; padding: 20px;">
    <h1 style="color: #333;">phpisfun</h1>
    <p style="color: #666;">Welcome to phpisfun! If you want you can view the source code <a href="?source">here</a>. Happy RCE :)</p>

    <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); display: inline-block; margin-top: 20px;">
        <form action="" method="POST">
            <input type="text" name="username" placeholder="insert username" required style="width: 80%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px;">
            <input type="submit" name="register" value="click" style="background-color: #28a745; color: white; border: none; padding: 10px 15px; border-radius: 5px; cursor: pointer; transition: 0.3s;">
        </form>
        <br>
        <p>
        <?php 
            if($command){
                // don"t show output, i don"t trust u :)
                // echo shell_exec($command);
                shell_exec($command);
                echo "Welcome user";
            }
        ?>
        </p>
    </div>
    
</body>
</html>
