ifndef $(VERSION)
VERSION=development
endif

set_version:
	echo "VERSION = '$(VERSION)'" > $(INSTALL_DIR)/VERSION

setup_ws:
	mkdir -p $(INSTALL_DIR)
	cp -r * $(INSTALL_DIR)
	source /opt/ros/humble/local_setup.bash
	cd $(INSTALL_DIR); colcon build

install_ros_ws: setup_ws set_version
