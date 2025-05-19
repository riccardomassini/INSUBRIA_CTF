#include <stdio.h>
#include <string.h>
#include <openssl/sha.h>
#include <stddef.h>

#define FLAG_SIZE 11

static const char flag[] = "04ded642e70268452fd1413837bd19554782fe458a4b778c07ffa3d83cf20758";

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

int main(int argc, char const *argv[])
{
    size_t len;
    if (argc != 2) {
        printf("Usage: %s <flag>\n", argv[0]);
        return 1;
    }
    len = strlen(argv[1]);
    if (len > FLAG_SIZE-1) {
        printf("Invalid flag size\n");
        return 1;
    }
    if (argv[1][len] != '\0') {
        printf("Invalid flag format\n");
        return 1;
    }
    if (!strcmp(sha((const char *)argv[1]), flag)) {
        printf("Correct flag!\n");
    } else {
        printf("Incorrect flag\n");
        return 1;
    }
    return 0;
}
