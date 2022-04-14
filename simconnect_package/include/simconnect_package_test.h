#ifndef __TEST_H
#define __TEST_H

#ifdef _WIN32
#define simconnect_package_EXPORT __declspec(dllexport)
#else
#define simconnect_package_EXPORT
#endif

simconnect_package_EXPORT void testSimConnect();

// simconnect_package_EXPORT class SimConnectTest;
// void testSimConnect();

#endif // __TEST_H