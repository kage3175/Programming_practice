#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node{
	int data;
	struct Node *next;
	struct Node *previous;
}Node;

typedef struct Dequeue{
	Node *front;
	Node *rear;
	int count;
}Dequeue;

void initDequeue(Dequeue *dequeue);
int is_empty(Dequeue *dequeue);
void push_front(Dequeue *dequeue, int data);
void push_back(Dequeue *dequeue, int data);
int front_value(Dequeue *dequeue);
int rear_value(Dequeue *dequeue);
int size(Dequeue *dequeue);
int pop_front(Dequeue *dequeue);
int pop_back(Dequeue *dequeue);

/*main �� �ڸ�*/


void initDequeue(Dequeue *dequeue){
	dequeue->front=NULL;
	dequeue->rear=NULL;
	dequeue->count=0;
}

int is_empty(Dequeue *dequeue){
	return dequeue->count==0;
}

void push_back(Dequeue *dequeue, int data){
	Node *newNode = (Node *)malloc(sizeof(Node));
	newNode->data=data;
	newNode->next=NULL;
	if(is_empty(dequeue)){//queue�� ������� �� 
		dequeue->front=newNode;
		newNode->previous=NULL;
	}
	else{
		newNode->previous=dequeue->rear;
		dequeue->rear->next=newNode;
	}
	dequeue->rear=newNode;
	dequeue->count++;
}

void push_front(Dequeue *dequeue, int data){
	Node *newNode = (Node *)malloc(sizeof(Node));
	newNode->data=data;
	newNode->previous=NULL;
	if(is_empty(dequeue)){//queue�� ������� �� 
		dequeue->rear=newNode;
		newNode->next=NULL;
	}
	else{
		newNode->next=dequeue->front;
		dequeue->front->previous=newNode;
	}
	dequeue->front=newNode;
	dequeue->count++;
}

int front_value(Dequeue *dequeue){
	if(is_empty(dequeue)) return -1;//������� -1 ��ȯ 
	return dequeue->front->data;
}

int rear_value(Dequeue *dequeue){
	if(is_empty(dequeue)) return -1;//������� -1 ��ȯ 
	return dequeue->rear->data;
}

int size(Dequeue *dequeue){
	return dequeue->count;
}

int pop_front(Dequeue *dequeue){//���� ù ���� ������, �� ���� ��ȯ�Ѵ�. 
	int data;
	Node *ptr;
	if(is_empty(dequeue)){
		return -1;
	}
	ptr=dequeue->front;
	data=ptr->data;
	dequeue->front=ptr->next;
	free(ptr);
	dequeue->count--;
	return data;
}

int pop_back(Dequeue *dequeue){//���� ù ���� ������, �� ���� ��ȯ�Ѵ�. 
	int data;
	Node *ptr;
	if(is_empty(dequeue)){
		return -1;
	}
	ptr=dequeue->rear;
	data=ptr->data;
	dequeue->rear=ptr->previous;
	free(ptr);
	dequeue->count--;
	return data;
}
