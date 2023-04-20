#include <stdio.h>
#include <stdlib.h>

char* fgets(FILE *fp, int n, char*s){
	register int c;
	register char* cs;
	cs=s;
	for(int i=0;i<n-1;i++){
		*cs=getc(fp);
		if(*cs=='\n') break;
		cs++;
	}
	*cs='\0';
	return (c==EOF&&cs==s)?NULL:s;
}

int main(void){
	FILE *fp;
	char str[100];
	fp=fopen("HGSS_pokemon.txt", "r");
	str=fgets(fp,6,str);
	fclose(fp);
	printf("%s\n", str);
	return 0;
}
