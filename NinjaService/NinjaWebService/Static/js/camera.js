import styles from '../css/camera_style.css'

export class CameraView extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
    };
  }
  componentDidMount() {
    var canvas = document.getElementById('camera_view');
    console.log(canvas);
    console.log(styles);
  }
  componentWillUnmount() {
  }
  render() {
    return (
      <canvas id="camera_view" className={"camera_view " + styles['camera_view']}>

      </canvas>
    );
  }
};
