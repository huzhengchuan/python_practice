#define _GNU_SOURCE_

#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
#include <sched.h>
#include <signal.h>
#include <unistd.h>

#define STACK_SIZE (1024*1024)

static char child_stack[STACK_SIZE];
char *const child_args[] = {
	"/bin/bash",
	NULL};

int child_main(void *arg) 
{
	printf("- world !\n");
	execv(child_args[0], child_args);
	printf("oops-\r\n");
	return 1;
}

int main()
{
	printf("- Hello\r\n");
	int child_pid = clone(child_main, child_stack + STACK_SIZE, SIGCHLD, NULL);
	waitpid(child_pid, NULL, 0);
	return 0;
}
