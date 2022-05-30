build:
	xhost +si:localuser:root
	docker build -t prl_rostorch:prl-message-passing-framework . 

run:
	docker container rm tas || true
	docker run \
		-it \
		-e "DISPLAY" \
		-e "QT_X11_NO_MITSHM=1" \
		-e "XAUTHORITY=${XAUTH}" \
		-e MPF_REALSENSE_ON \
		-v ~/.Xauthority:/root/.Xauthority:rw \
		-v "/tmp/.X11-unix:/tmp/.X11-unix:rw" \
		-v /dev:/dev \
		-v /etc/hosts:/etc/hosts \
		-e ROS_MASTER_URI=http://10.0.0.107:11311 \
		-e ROS_IP=10.0.0.107 \
		-v $(MPF_REPO_PATH)/tas_perception/:/ros-ws/src/tas_perception/ \
		--network host \
		--privileged \
		--runtime=nvidia \
		--name tas \
		prl_rostorch:prl-message-passing-framework
