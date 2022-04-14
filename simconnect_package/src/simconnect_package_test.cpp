#include "simconnect_package_test.h"
#include <Windows.h>
#include "SimConnect.h"
#include <iostream>

void testSimConnect()
{
    HANDLE sc = NULL;
    if (SUCCEEDED(SimConnect_Open(&sc, "Test Client", NULL, 0, 0, 0)))
    {
        std::cout << "Connected to SimConnect, now closing" << std::endl;
        SimConnect_Close(sc);
    }
    else
    {
        std::cout << "Failed to open SimConnect connection" << std::endl;
        std::cout << "Make sure you have an instance of Prepar3D running" << std::endl;
    }
}