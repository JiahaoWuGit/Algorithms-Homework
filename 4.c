#include<stdio.h>
#include <sys/time.h>
int besttime = 9999;
int cost[8] = {0};//used to record the time of three machine
int plan[19] = {0};//used to store every task's machine
int bestplan[19] = {0};
int machine[3] = {3,5,8};
int taskNum[3] = {10,15,19};
int test0[10] = {47, 20, 28, 44, 21, 45, 30, 39, 28, 33};//112
int test1[15] = {98, 84, 50, 23, 32, 99, 22, 76, 72, 61, 81, 39, 76, 54, 37};//182
int test2[19] = {39, 39, 23, 45, 100, 69, 21, 81, 39, 55, 20, 86, 34, 53, 58, 99, 36, 45, 46};//126
int max(int choice)
{
    int i;
    int maxcost=0;
    for(i=0; i<machine[choice];i++)
    {
      if(cost[i]>maxcost)
            maxcost = cost[i];
    }
  //  printf("maxcost:%d\n",maxcost);
    return maxcost;
}
int arrange(int curr, int test, int* task)
{//  printf("%d\n",curr);
  if(max(test) >= besttime)// There is no need to search deeper, because the time is longer than current besttime
          return 0;
  if(curr == taskNum[test])//search to the end of the nodes
  {
     if(max(test) < besttime)
     {
       besttime = max(test);
       int kl;
       for(kl=0;kl<taskNum[test];kl++)//i represent which machine the current task is on
       {
         bestplan[kl] = plan[kl];
       }
     }
     return besttime;
  }
  int i;
  for(i=0;i<machine[test];i++)//i represent which machine the current task is on
  {
      cost[i] += task[curr];
      plan[curr] = i;
      arrange(curr+1, test, task);
      plan[curr] = 0;
      cost[i] -= task[curr];
      if(cost[i] == 0)//there is no need to search the next common way
        return besttime;
  }
  return besttime;
}
int printResult(int choice)
{
  int i;
  printf("The format of the printed task list:( number of the trask:the time this task needs)\n");
  for(i=0;i<machine[choice];i++)
  {
    printf("The %d machine:\n",i);
    int j;
    for(j=0;j<taskNum[choice];j++)
    {
      if(bestplan[j]==i)
      {
        switch(choice)
        {
          case 0: printf("%d:%d ",j,test0[j]);break;
          case 1: printf("%d:%d ",j,test1[j]);break;
          default: printf("%d:%d ",j,test2[j]);break;
        }//switch
      }//if
    }//for
    printf("\n");
  }//for
  return 0;
}
int main()
{
  struct timeval start, end;
  int choice;
  printf("please enter which test example you want:\n0)n = 10, k = 3  1)n = 15, k = 5  2)n = 19, k = 8\n");
  scanf("%d",&choice);
  gettimeofday( &start, NULL );
  switch (choice)
  {
      case 0:   arrange(0,choice,test0); break;
      case 1:   arrange(0,choice,test1); break;
      default:   arrange(0,choice,test2);
  }
  gettimeofday( &end, NULL );
  int timeuse = 1000000 * ( end.tv_sec - start.tv_sec ) + end.tv_usec - start.tv_usec;
  printResult(choice);
  printf("The best schedule's cost of time is %d\n",besttime);
  double timeused = (double)timeuse/1000000;
  printf("time used to run the exe: %lf s\n", timeused);
  return 0;
}
