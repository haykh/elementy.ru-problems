var fps = 30;
var capturer = new CCapture({ format: 'png', framerate: fps });


function setup() {
  createCanvas(320, 480);
  frameRate(fps);
}

function drawPulse(L, z1, z2) {
  let ni = 150;
  let a = 10, w = 10;
  beginShape();
  for (let z = -L; z < L; z += L / ni) {
    let dz1 = (z - z1) / w;
    let dz2 = (z - z2) / w;
    let d = a * (Math.exp(-Math.pow(dz1, 2)) + Math.exp(-Math.pow(dz2, 2)));
    vertex(d, z);
  }
  endShape();
}

function bc(L, z) {
  if (z < -L) {
    z = -L;
  }
  if (z > L) {
    z = L;
  }
  return z
}

function drawLine(L, z1, z2) {
  z1 = bc(L, z1)
  z2 = bc(L, z2)
  background(220);

  translate(width / 2, height / 2);
  stroke(50);
  strokeWeight(10);
  line(-L / 2, -L, L / 2, -L)
  stroke(10);
  noFill();
  strokeWeight(2);
  drawPulse(L, z1, z2);
}

var startMillis;
const duration = 8000;

let time = 0, dt = 0.01, g = 100, L = 200;
let z1 = 0, z2 = 0, counter = 0;
function draw() {
  if (frameCount === 1) {
    capturer.start();
  }
  if (startMillis == null) {
    startMillis = millis();
  }
  var elapsed = millis() - startMillis;
  var t = map(elapsed, 0, duration, 0, 1);
  if (t > 1) {
    noLoop();
    console.log('finished recording.');
    capturer.stop();
    capturer.save();
    return;
  }

  time += dt;
  counter += 1;
  drawLine(L, z1, z2);

  let vz1 = sqrt(g * (L - z1));
  if (vz1 > 0.1) {
    z1 = L - 0.25 * (4 * L - 4 * sqrt(g * L) * time + g * time * time);
  }

  let vz2 = sqrt(g * (L - z2));
  if (vz2 > 0.1) {
    z2 = L - 0.25 * (4 * L + 4 * sqrt(g * L) * time + g * time * time);
  }
  // console.log(time)
  capturer.capture(document.getElementById('defaultCanvas0'));
}