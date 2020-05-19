#include<stdio.h>
int main(){
int x,cpt,i
do{
puts(“Entrer un nombre”)
scanf(“%d”,&x);
}while(x<=0)
cpt=2;
for(i=2;i<x;i++){
if(x%i==0){
cpt++;
break;
}
}
if(cpt!=2){
	printf(“%d est un nombre premier”,x);
}else{
printf(“%d n’est pas un nombre premier”,x);
}
rreturn 0
}
