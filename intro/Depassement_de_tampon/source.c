void shell(void)
{
  puts("Enjoy your shell!");
  system("/bin/bash");
  return;
}

int main(void)
{
  int input;
  time_t seed;
  char buf[36];
  int tot;
  uint r1;
  uint r2;
  
  seed = time(0);
  srand(seed);
  r1 = rand();
  r2 = rand();
  tot = r1 + r2;
  printf(">>> %d + %d = ", r1, r2);
  fflush(stdout);
  fgets(buf, 100, stdin);
  input = atoi(buf);
  if (tot == input) {
    puts("Yes!");
  }
  else {
    puts("No!");
  }
  return 0;
}
