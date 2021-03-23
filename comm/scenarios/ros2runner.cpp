#include "nodestarter.h"
#include <ros2node/ros2nodefactory.h>

int main(int argc, char *argv[])
{
    NodeFactoryInterfacePtr factory(new Ros2NodeFactory());
    return nodestarter::startNode(argc, argv, factory);
}
