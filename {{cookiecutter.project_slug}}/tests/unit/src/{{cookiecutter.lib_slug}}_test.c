#define CTEST_MAIN

#include "ctest.h"

CTEST({{cookiecutter.lib_slug}}_test, test)
{
  // Do Nothing.
}

int
main(int argc, const char *argv[])
{
  const int result = ctest_main(argc, argv);
  return result;
}
