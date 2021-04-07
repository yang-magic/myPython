#include <stdio.h>
void swap(int A[],int i,int j){
	int temp=A[i];
	A[i]=A[j];
	A[j]=temp;
}

void printA(int a[],int n){
	//int i;
	//for(i=0;i<n;i++){
	//	printf("%d ",A[i]);
	//}
	if((a[0]*100+a[1]*10+a[2]+a[3]*100+a[4]*10+a[5])==(a[6]*1000+a[7]*100+a[8]*10+a[9])){
		if(a[6]==0){
			printf("%d+%d=0%d",a[0]*100+a[1]*10+a[2],a[3]*100+a[4]*10+a[5],a[6]*1000+a[7]*100+a[8]*10+a[9]);
			printf("\n");
		}
		else{
			printf("%d+%d=%d",a[0]*100+a[1]*10+a[2],a[3]*100+a[4]*10+a[5],a[6]*1000+a[7]*100+a[8]*10+a[9]);
			printf("\n");
		}	
	}
	//printf("\n");
}

void perm(int A[],int p,int q){
	if(p==q){
		printA(A,q+1);
	}
	else{
		int i;
		for(i=p;i<=q;i++){
			swap(A,p,i);
			perm(A,p+1,q);
			swap(A,p,i);
		}
	}
}

int main() {
	int A[10]={1,2,3,4,5,6,7,8,9,0};
	perm(A,0,9);
	return 0;
}
