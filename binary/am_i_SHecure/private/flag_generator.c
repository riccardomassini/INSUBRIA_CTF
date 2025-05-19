#include <stdio.h>
#include <openssl/sha.h>
#include <string.h>

#define FLAG_SIZE 11
const char flag[FLAG_SIZE] = "flag{e42#}";

char * sha(const char *input)
{
    /* Allocate memory for the result string (64 characters for SHA-256 hex representation + 1 for null terminator) */
    static char hex_hash[65];
    unsigned short i;
    /* SHA-256 hash result */
    unsigned char hash[SHA512_DIGEST_LENGTH];

    /* Compute the SHA-256 hash */
    SHA256_CTX sha256_ctx;
    SHA256_Init(&sha256_ctx);  /* Initialize SHA-256 context */
    SHA256_Update(&sha256_ctx, input, strlen(input));  /* Process the input string */
    SHA256_Final(hash, &sha256_ctx);  /* Finalize and get the hash */

    /* Convert the binary hash to a hex string */
    for (i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        snprintf(&hex_hash[i*2], 3, "%02x", hash[i]);  /* Convert each byte to 2 hex chars */
    }
    
    return hex_hash;  /* Return the resulting hex string */
}

int main()
{
    printf("SHA1 of flag: %s\n", sha(flag));
    return 0;
}
