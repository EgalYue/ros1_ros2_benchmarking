#/bin/bash

. ./scripts/networks.sh
cmd="source /ros2_ws/install/setup.sh && cd /opt/rti.com/rti_connext_dds-5.3.1/resource/scripts && source ./rtisetenv_x64Linux3gcc5.4.0.bash && cd /ros2_benchmarking/comm/build/scenarios && ./ros2runner rosrobot.ini >/logs/robot.txt 2>&1"
docker run -d -h robot --pid=host --net ros2connext --ip $net_ros2connext_robot --add-host console:$net_ros2connext_console -v $PWD/logs:/logs ros2:connext bash -c "$cmd"
