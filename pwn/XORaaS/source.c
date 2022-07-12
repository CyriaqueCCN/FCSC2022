void xor(byte *buf) // at 0x0040115f
{
  byte buf2 [140];
  int i;
  
  fread(buf2, 1, 145, stdin);
  for (i = 0 ; i < 128 ; i++) {
    *(byte *)(buf + i) = buf2[i] ^ *(byte *)(buf + i);
  }
  return;
}

void shell(void) // at 0x00401142
{
  execve("/bin/bash", 0, 0);
  return;
}

int main(void) // at 0x004011d
{
  byte  buf[128];
  
  fread(args, 1, 128, stdin);
  xor(buf);
  fwrite(buf, 1, 128, stdout);
  return 0;
}
