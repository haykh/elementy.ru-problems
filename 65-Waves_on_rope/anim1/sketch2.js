var fps = 30;
var capturer = new CCapture({ format: 'png', framerate: fps });


function setup() {
  createCanvas(320, 480);
  frameRate(fps);
}

function drawPulse(L, z0, flag=false) {
  let ni = 150;
  let a = 10, w = 10;
  let d;
  beginShape();
  for (let z = -L; z < L; z += L / ni) {
    let dz0 = (z - z0) / w;
    d = a * (Math.exp(-Math.pow(dz0, 2)));
    vertex(d, z);
  }
  endShape();

  if (flag) {
    fill(50);
    circle(d, L + 25, 50);
  }
}

function bc(L, z) {
  if (z < -L) {
    z = -L;
  }
  // if (z > L) {
  //   z = L;
  // }
  return z
}

function drawLines(L, z1, z2) {
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

  translate(-50, 0);
  drawPulse(L, z1);

  translate(100, 0);
  drawPulse(L, z2, true);
}

var startMillis;
const duration = 7000;

let time = 0, dt = 0.02, g = 100, L = 200;
let z1 = L, z2 = L, counter = 0, C = 2;
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
    // capturer.save();
    return;
  }

  time += dt;
  counter += 1;
  drawLines(L, z1, z2);

  let vz1 = sqrt(g * (L - z1));
  z1 = L - 0.25 * g * time * time;
  console.log(vz1);

  let vz2 = sqrt(g * (L - z2));
  z2 = L - 0.25 * g * time * time - sqrt(g * C) * time;
  capturer.capture(document.getElementById('defaultCanvas0'));
}