int main() {
    int vetor[] = {3, 8, 11, 20, 7};
    int i, par;
    par = 0;
    for (i = 0; i < 5; i++) {
        if (vetor[i] % 2 == 0) {
            par++;
        }
    }
    printf("%d\n", par);
}
