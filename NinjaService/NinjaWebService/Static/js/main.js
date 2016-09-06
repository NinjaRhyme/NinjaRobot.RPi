import { InputView } from './input.js'
import { CameraView } from './camera.js'

export class MainView extends React.Component {
  constructor(props) {
    super(props);

  }

  render() {
    return (
      <div className="main_view">
        <CameraView/>
        <InputView/>
      </div>
    );
  }
};
