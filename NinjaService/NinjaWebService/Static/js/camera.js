import styles from '../css/camera_style.css'

export class CameraView extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      ws: new WebSocket("ws://" + location.host + "/camera")
    };
    this.state.ws.onopen = function(event) {
        console.log("camera ws connected");
    };
    this.state.ws.onmessage = function(event) {
        var data = JSON.parse(event.data);
        // Todo
    };
  }
  componentDidMount() {
    var canvas = document.getElementById('camera_view');
		var ctx = canvas.getContext('2d');
    ctx.fillStyle = 'red';
		ctx.fillText('loading...', canvas.width/2-30, canvas.height/3);
		var player = new jsmpeg(this.state.ws, {canvas:canvas});
  }
  componentWillUnmount() {
  }
  render() {
    return (
      <canvas id="camera_view" className={"camera_view"}>

      </canvas>
    );
  }
};
