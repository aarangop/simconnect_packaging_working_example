#pragma once

#ifdef _WIN32
#define simconnect_consumer_EXPORT __declspec(dllexport)
#else
#define simconnect_consumer_EXPORT
#endif

simconnect_consumer_EXPORT void simconnect_consumer();
simconnect_consumer_EXPORT void consumer_testSimConnect();
