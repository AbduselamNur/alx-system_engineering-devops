#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

/**
 * infinite_while - runs forever and returns nothing
 * Return: 0 for sucess
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - a program that creates 5 zombie process
 * Return: 0 for success
 */
int main(void)
{
	int child = 0;
	pid_t pid;

	while (child < 5)
	{
		pid = fork();
		if (!pid)
			break;
		printf("Zombie process created, PID: %i\n", (int)pid);
		child++;
	}
	if (pid != 0)
	{
		infinite_while();
	}
	return (0);
}
