#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
	FILE *fp;
	char pokemon[300][3][18];
	char line[50];
	char *ptr;
	fp=fopen("HGSS_pokemon.txt", "r");
	int num=0;int flag=0;
	while(1){
		int i=0;
		if(fgets(line,49,fp)==NULL) break;
		ptr=strtok(line,"\t");
		while(ptr!=NULL){
			strcpy(pokemon[num][i], ptr);
			i++;
			ptr=strtok(NULL,"\t");
		}
		pokemon[num][2][strlen(pokemon[num][2])-1]='\0';
		//printf("%s %s %s\n", pokemon[num][0], pokemon[num][1], pokemon[num][2]);
		num++;		
	}
	
	while(1){
		flag=1;
		scanf("%s", line);
		for(int i=0;i<num;i++){
			if(strcmp(line,pokemon[i][0])==0){
				printf("%s의 타입: %s %s\n",pokemon[i][0], pokemon[i][1], pokemon[i][2]);
				flag=0;
				break;
			}
		}
		if(flag) printf("그런 이름의 포켓몬이 없습니다.\n");
	}
	
	return 0;
}
