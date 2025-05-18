# am i SHecure?

1. Decompilare il file `SHecure`.
2. Capire da quanti caratteri è formata la flag e come viene comparata.
3. La flag è composta da 11 caratteri e viene cifrata in **SHA256**.
4. Sapendo che la flag inizia con `flag{` e finisce con `}` si escludono 6 caratteri, usando l'indizio nella descrizione si apprende che il primo carattere è `e`, dunque la flag sarà così composta: `flag{eXXXX}`.
5. E' possibile fare un bruteforce su 4 caratteri.
6. L'hash della flag è contenuto nel file compilato.
7. Scrivere un exploit che cicli i 4 caratteri ignoti su tutti i caratteri stampabili, hashare le stringhe con **SHA256** e compararle con l'hash del file finché non combacia.
8. Una volta ottenuto un match si è ottenuta una flag.
