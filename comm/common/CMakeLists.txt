cmake_minimum_required(VERSION 3.5.1)
project(common)

set(SOURCES
    logging.cpp
    communicationutils.cpp)

set(HEADERS
    communicationutils.h
    logging.h
    nodeinterface.h
    messagetypes.h
    topics.h
    nodefactoryinterface.h
    qosprofiles.h
    settings.h)

add_library(common SHARED ${SOURCES} ${HEADERS})
target_link_libraries(common Qt5::Core)
INSTALL(FILES ${HEADERS} DESTINATION /include/common)
INSTALL_TARGETS(/lib RUNTIME_DIRECTORY /lib common)

