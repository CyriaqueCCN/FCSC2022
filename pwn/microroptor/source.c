// Le binaire est strippé mais on suit l'entry jusqu'à trouver ceci :

undefined8 FUN_00101178(void)
{
  int iVar1;
  char local_28 [32];
  
  printf("%p\n",&PTR_s_m3t4ll1cA_00104010);
  read(0,local_28,0x200);
  iVar1 = strncmp(local_28,PTR_s_m3t4ll1cA_00104010,9);
  if (iVar1 == 0) {
    puts("Welcome back master (of puppets)!");
  }
  else {
    puts("Nope, you are no master.");
  }
  return 0;
}
