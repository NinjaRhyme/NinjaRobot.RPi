window.onload=function() {
  var ws = new WebSocket("ws://" + location.host + "/input");
  ws.onopen = function(event) {
      console.log("ws connected");
  };
  ws.onmessage = function(event) {
      var data = JSON.parse(event.data);
      // Todo
  };

  var keysDown = {};
  addEventListener("keydown", function (e) {
      keysDown[e.keyCode] = true;
      ws.send(JSON.stringify({
          "key": e.keyCode
      }));
  }, false);
  addEventListener("keyup", function (e) {
      delete keysDown[e.keyCode];
  }, false);
}
