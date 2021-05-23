var ros = new ROSLIB.Ros({
	url : 'ws://192.168.1.184:9090'
});

ros.on('connection', function(){
	console.log('Connected to websocket server.');
});

ros.on('error', function(error){
	console.log('Error connecting to websocket server:', error);
});

ros.on('close', function(){
	console.log('Connected to websocket server closed.');
});

// Publishing Topic "to_robot2_cmd"
// ------------------
var robot_2_Cmd = new ROSLIB.Topic({
	ros : ros,
	name : 'to_robot2_cmd',
	messageType : 'std_msgs/String'
});

function forward_2() {
    var cmd = new ROSLIB.Message({
    	data : 'forward'
    });
    robot_2_Cmd.publish(cmd);
}
function back_2() {
    var cmd = new ROSLIB.Message({
    	data : 'back'
    });
    robot_2_Cmd.publish(cmd);
}
function left_2() {
    var cmd = new ROSLIB.Message({
    	data : 'left'
    });
    robot_2_Cmd.publish(cmd);
}
function right_2() {
    var cmd = new ROSLIB.Message({
    	data : 'right'
    });
    robot_2_Cmd.publish(cmd);
}
function home_2() {
    var cmd = new ROSLIB.Message({
        data : 'home'
    });
    robot_2_Cmd.publish(cmd);
}
function stop_2() {
    var cmd = new ROSLIB.Message({
        data : 'stop'
    });
    robot_2_Cmd.publish(cmd);
}