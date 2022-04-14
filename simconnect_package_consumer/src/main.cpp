// #include "simconnect_package_test.h" --> using testSimConnect() from simconnect_package fails with unresolved external symbol.
#include <iostream>
#include "simconnect_consumer.h"

int main()
{
    consumer_testSimConnect(); // --> Consuming preocompiled SimConnect libraries works!
    // testSimConnect(): -->    // --> Consuming simconnect_package directly fails with unresolved external symbol, since simconnect_package.lib is not linked!
}
