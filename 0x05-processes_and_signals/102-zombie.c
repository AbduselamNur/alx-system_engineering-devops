#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
int main(void)
{
	int children = 0;
	pid_t p_id;

	while (children < 5)
	{
		p_id = fork();
		if (!p_id)
			break;
		printf("Zombie process created, PID: %i\n", (int)p_id);
		children++;
	}
	if (p_id != 0)
	{
		infinite_while();
	}
	return (0);
}
