#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SORT_NUM 1000
#define DIGIT_SORT_NUM 3
int field[SORT_NUM+1] ={0};

void shuffle(int arr[],int loc1,int loc2);
int generate_randnum(void);


int main(void){
	int shuf1=0;int shuf2=0;
	srand(time(NULL));
	for(int i=1;i<=SORT_NUM;i++) field[i] = i;
	for(int i=1;i<=SORT_NUM*2; i++){
		shuf1 = generate_randnum();
		shuf2 = generate_randnum();
		shuffle(field, shuf1, shuf2);
	}
	
	for(int i=1;i<=10;i++){
		printf("%d ", field[i]);
	}
	
	return 0;
}

void shuffle(int arr[], int loc1, int loc2){
	int temp=0;
	temp=arr[loc1];
	arr[loc1]=arr[loc2];
	arr[loc2]=temp;
	return;
}

int generate_randnum(void){
	int num=0;
	for(int i=0;i<DIGIT_SORT_NUM;i++){
		num = 10*num + (rand()%10);
	}
	return num+1;
}
