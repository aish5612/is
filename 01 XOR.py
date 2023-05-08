for(int i=0;i<len;i++){
        int original, modified;
        original = str[i];
        modified = str[i]^127;
        printf("i %d char %c orig %02x mod %02x\n", i, original, original, modified);
}