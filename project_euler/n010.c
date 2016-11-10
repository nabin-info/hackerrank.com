#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

long *N = NULL;
long Nmax = 0;

long *sieve(long n) {
    long np1 = n+1;
    long nrt = (int) sqrtf((float)np1)+0.5;
    long *P = malloc((size_t)(np1+1) * sizeof(long));

    for (long i = 0; i < np1; i+=1) P[i] = i;
    for (long i = 4; i < np1; i+=2) P[i] = 0;
    P[1] = 0;
    for (long i = 3; i < np1; i+=2) {
        if (P[i]) {
            for (long j = i*i; j < np1; j += i) {
                /* printf("Testing: %3d\n", j); */
                P[j] = 0;
            }
        }
    }

    /*
    for (int i = 1; i < np1; i++) {
        if (P[i]) {
            printf("%d, ", P[i]);
        }
    }
    printf("\n");
    */
    return P;
}

long *psums(long n, long *P) {
    long np1 = n+1;
    long nrt = (int) sqrtf((float)np1)+0.5;
    long *S = malloc((size_t)(np1+1) * sizeof(long));
    long s = 0;
    for (long i = 0; i < np1; i+=1) {
        s += P[i];
        S[i] = s;
    }
    return S;
}


int main(){
    long t; 
    N = malloc((size_t)(t+1) * sizeof(long));
    scanf("%ld",&t);
    for(long a0 = 0; a0 < t; a0++) {
        long n;
        scanf("%ld", &n);
        N[a0] = n;
        if (n > Nmax) 
            Nmax = n;
    }
    long *p = sieve(Nmax);
    long *s = psums(Nmax,p);
    for (long i = 0; i < t; i++) {
        long nm1 = N[i];
        /*
        long s = 0;
        for (long j = 0; j <= nm1; j++) {
            if (p[j])
                s += p[j];
        }
        */
        printf("%ld\n", s[nm1]);
    }
    return 0;
}

