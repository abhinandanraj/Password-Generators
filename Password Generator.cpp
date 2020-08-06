#include <stdio.h> 
#include <stdlib.h> 
#include<time.h> 
int main(void) 
{  srand(time(0));
   int input;
   char randomarray[]={'A','1','B','2','C','3','D','4','E','5','F','6','G','7','H','8','I','9','K','0','L','M','!','n','@','o','#','p','$','q','^','R','8','s','&','t','u','/','5','2','3','w','*','5','y','z','?','8','r','a','b','#','$','%','*','4','T','f','g'};
    
    printf("Enter the length: \n");
    scanf("%d",&input);
    printf("Your Password: ");
    for(int i=0;i<=input;i++)
    printf("%c",randomarray[rand()%60]);
}
