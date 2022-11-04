#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define size 4

void board_print(int arr[][5]){
	int i=0;int j=0;
	for(i=0;i<size;i++){
		for(j=0;j<size;j++){
			if (arr[i][j]>=1000) printf("%d", arr[i][j]);
			else if(arr[i][j]>=100) printf(" %d", arr[i][j]);
			else if(arr[i][j]>=10) printf("  %d", arr[i][j]);
			else printf("   %d", arr[i][j]);
		}
		printf("\n\n");
	}
	printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
}

int* turn_left(int arr[][5], int n){//현재 arr, 돌릴 횟수 전달 
	int temp[5][5]={0};
	int i=0;int j=0;
	if(n==0){
		return(int*) arr;
	}
	for(i=0;i<size;i++){
		for(j=0;j<size;j++){
			temp[i][j]=arr[j][3-i];
		}
	}
	turn_left(temp, n-1);
}//End of turn_left function

int* push_left(int arr[][5]){
	int i=0; int j=0;
	int mostleft=5;
	for(i=0;i<size;i++){
		for(j=0;j<size;j++){
			if(arr[i][j]==0&&mostleft>j) mostleft=j;
			if(arr[i][j]!=0&&mostleft!=5){
				 arr[i][mostleft]=arr[i][j];
				 arr[i][j]=0;
				 mostleft++;
			}
		}
		mostleft=5;
	} 
	return(int*) arr;
}//end of push_left function

int gameover(int arr[][5]){
	int i=0;int j=0;int temp=1;
	for(i=0;i<size;i++){
		for(j=0;j<size;j++){
			if(arr[i][j]==0){
				temp=0;
				break;
			}
			if(arr[i][j]==arr[i][j+1]||arr[i][j]==arr[i+1][j]){
				temp=0;
				break;
			}
		}
	}
	if(temp==1) return 1;
	else return 0;
}

int* find_zero(int arr[][5], int counting[][2]){
	int i=0;int j=0;int temp=0;
	for(i=0;i<17;i++){
		for(j=0;j<2;j++) counting[i][j]=5;
	}
	for(i=0;i<size;i++){
		for(j=0;j<size;j++){
			if(arr[i][j]==0){
				counting[temp][0]=i;
				counting[temp][1]=j;
				temp++;
			}
		}
	}
	/*for(i=0;i<17;i++){
		for(j=0;j<2;j++){
			printf("%d ",counting[i][j]);
		}
		printf("\n");
	}*/
	return(int*) counting;
}

int* adding(int arr[][5],int* tempscore){
	int i=0; int j=0;
	int temp[5][5]={0};
	for(i=0;i<size;i++){
		for(j=0;j<size-1;j++){
			if(arr[i][j]==arr[i][j+1]){
				*(tempscore)=*(tempscore)+arr[i][j];
				arr[i][j]=arr[i][j]*2;
				arr[i][j+1]=0;
			}
		}
	}
	for(i=0;i<size;i++){
		for(j=0;j<size;j++){
			temp[i][j]=arr[i][j];
		}
	}
	return(int*) temp;
}

int errorcheck(int arr[][5],int temparr2[][5]){
	int i=0;int j=0;int temp=0;
	for(i=0;i<size;i++){
		for(j=0;j<size;j++){
			if(arr[i][j]!=temparr2[i][j]){
				temp=1;
				break;
			}
		}
	}
	return temp;
}

int main(void){
	int arr[5][5]={0}; int* temp; int temparr2[5][5]={0}; int counting[17][2];int score=0;
	int notvisited[17][2];
	int cnt_0=0; int insertwhere=0;
	char key=0;
	int randomx=0;int randomy=0;int i=0;int j=0;int two_or_four=0;int tempscore=0;
	
	srand(time(NULL));
	randomx=rand()%4;
	randomy=rand()%4;
	two_or_four=rand()%10;
	
	if (two_or_four<2) arr[randomx][randomy]=4;
	else arr[randomx][randomy]=2;
	board_print(arr);
	
	while (1){
		tempscore=0;
		if(gameover(arr)){
			printf("Game Over!\n최종 점수는: %d 점", score); 
			break;
		}
		key=getchar();
		while(getchar()!='\n'){}
		if(key=='w'){
			temp=turn_left(arr,1);
			for(i=0;i<size;i++){
				for(j=0;j<size;j++) temparr2[i][j]=*(temp+5*i+j);
			}
			temp=push_left(temparr2);
			for(i=0;i<size;i++){
				for(j=0;j<size;j++) temparr2[i][j]=*(temp+5*i+j);
			}
			temp=adding(temparr2, &tempscore);
			for(i=0;i<size;i++){
				for(j=0;j<size;j++) temparr2[i][j]=*(temp+5*i+j);
			}
			temp=push_left(temparr2);
			for(i=0;i<size;i++){
				for(j=0;j<size;j++) temparr2[i][j]=*(temp+5*i+j);
			}
			temp=turn_left(temparr2,3);
			for(i=0;i<size;i++){
				for(j=0;j<size;j++) temparr2[i][j]=*(temp+5*i+j);
			}
			if(errorcheck(arr,temparr2)==0){
				printf("잘못된 입력입니다\n");
				board_print(arr);
				continue;
			}
			score=score+tempscore;//스코어 갱신 
			for(i=0;i<size;i++){//arr에 다시 갑 대입 
				for(j=0;j<size;j++) arr[i][j]=temparr2[i][j];
			}
		}
		if(key=='s'){
			temp=turn_left(arr,3);
			for(i=0;i<size;i++){
				for(j=0;j<size;j++) temparr2[i][j]=*(temp+5*i+j);
			}
			temp=push_left(temparr2);
			for(i=0;i<size;i++){
				for(j=0;j<size;j++) temparr2[i][j]=*(temp+5*i+j);
			}
			temp=adding(temparr2,&tempscore);
			for(i=0;i<size;i++){
				for(j=0;j<size;j++) temparr2[i][j]=*(temp+5*i+j);
			}
			temp=push_left(temparr2);
			for(i=0;i<size;i++){
				for(j=0;j<size;j++) temparr2[i][j]=*(temp+5*i+j);
			}
			temp=turn_left(temparr2,1);
			for(i=0;i<size;i++){
				for(j=0;j<size;j++) temparr2[i][j]=*(temp+5*i+j);
			}
			if(errorcheck(arr,temparr2)==0){
				printf("잘못된 입력입니다\n");
				board_print(arr);
				continue;
			}
			score=score+tempscore;//스코어 갱신 
			for(i=0;i<size;i++){//arr에 다시 갑 대입 
				for(j=0;j<size;j++) arr[i][j]=temparr2[i][j];
			}
		}
		if(key=='d'){
			temp=turn_left(arr,2);
			for(i=0;i<size;i++){
				for(j=0;j<size;j++) temparr2[i][j]=*(temp+5*i+j);
			}
			temp=push_left(temparr2);
			for(i=0;i<size;i++){
				for(j=0;j<size;j++) temparr2[i][j]=*(temp+5*i+j);
			}
			temp=adding(temparr2,&tempscore);
			for(i=0;i<size;i++){
				for(j=0;j<size;j++) temparr2[i][j]=*(temp+5*i+j);
			}
			temp=push_left(temparr2);
			for(i=0;i<size;i++){
				for(j=0;j<size;j++) temparr2[i][j]=*(temp+5*i+j);
			}
			temp=turn_left(temparr2,2);
			for(i=0;i<size;i++){
				for(j=0;j<size;j++) temparr2[i][j]=*(temp+5*i+j);
			}
			if(errorcheck(arr,temparr2)==0){
				printf("잘못된 입력입니다\n");
				board_print(arr);
				continue;
			}
			score=score+tempscore;//스코어 갱신 
			for(i=0;i<size;i++){//arr에 다시 갑 대입 
				for(j=0;j<size;j++) arr[i][j]=temparr2[i][j];
			}
		}
		if(key=='a'){
			for(i=0;i<size;i++){
				for(j=0;j<size;j++) temparr2[i][j]=arr[i][j];
			}
			temp=push_left(temparr2);
			for(i=0;i<size;i++){
				for(j=0;j<size;j++) temparr2[i][j]=*(temp+5*i+j);
			}
			temp=adding(temparr2,&tempscore);
			for(i=0;i<size;i++){
				for(j=0;j<size;j++) temparr2[i][j]=*(temp+5*i+j);
			}
			temp=push_left(temparr2);
			for(i=0;i<size;i++){
				for(j=0;j<size;j++) temparr2[i][j]=*(temp+5*i+j);
			}
			if(errorcheck(arr,temparr2)==0){
				printf("잘못된 입력입니다\n");
				board_print(arr);
				continue;
			}
			score=score+tempscore;//스코어 갱신 
			for(i=0;i<size;i++){//arr에 다시 갑 대입 
				for(j=0;j<size;j++) arr[i][j]=temparr2[i][j];
			}
		}
		temp=find_zero(arr, counting);//여기부터는 랜덤자리에 2 삽입 
		cnt_0=0;
		for(i=0;i<17;i++){
			if(*(temp+2*i)==5) break;
			cnt_0++;
		}
		insertwhere=rand()%cnt_0;
		arr[*(temp+2*insertwhere)][*(temp+2*insertwhere+1)]=2;//일단은 2만 삽입
		board_print(arr);
	}

	/*temp=turn_left(arr,1);//이하 4줄은 왼쪽으로 한 바퀴 돌리는 것
	for(i=0;i<size;i++){
		for(j=0;j<size;j++) temparr2[i][j]=*(temp+5*i+j);
	}*/
	
		
	return 0;
}
