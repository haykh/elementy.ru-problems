var fps = 30;

const K0 = 1;
const Omega0 = 10;
const A0 = 30, W0 = 10;

function drawSin(L, k, t) {
  t = t % (2 * L / W0);

  let ni = 150;
  beginShape();
  ampl = A0 * Math.exp(-Math.pow(k * W0 / (2 * K0), 2)) * W0 / 5;
  // ampl *= cos(k * Omega0 * t / K0);
  ampl /= sqrt(2) * K0;
  for (let z = -L; z < L; z += L / ni) {
    let d = ampl * Math.sin(Omega0 * (Math.pow(k, 1.0) / K0) * t - k * z);
    // let d = ampl * Math.sin( - k * z);
    vertex(d, z);
  }
  endShape();
}

function drawModes(L, time) {
  stroke(10);
  noFill();
  strokeWeight(2);

  for (let k = 0.1; k <= 0.4; k += 0.1) {
    push();
    translate(width / 2 - 300 + ((k - 0.1) / 0.1) * 130, height / 2);
    drawSin(L, k, time);

    push();
    strokeWeight(1);
    noStroke();
    fill(0);
    textFont('monospace', 20);
    if (k != 0.4) {
      text('+', 50, 0);
    } else {
      text('+ ... =', 50, 0);
    }
    pop();

    pop();
  }
}

function drawPulse(L, t) {
  t = t % (2 * L / W0);

  push();
  translate(width / 2 + 300, height / 2);

  stroke(10);
  noFill();
  strokeWeight(2);

  let ni = 150;
  beginShape();
  for (let z = -L; z < L; z += L / ni) {
    let d = A0 * Math.exp(-Math.pow((Omega0 * t - K0 * (z + L)) / (W0 + 0 * t), 2))
    vertex(d, z);
  }
  endShape();
  pop();
}

let time = 0, dt = 0.2, L = 200;

var button;
var play = false;

function startPlaying() {
  play = true;
}

function setup() {
  createCanvas(720, 480);
  frameRate(fps);

  background(220);

  button = createButton("play");

  // Position the button
  button.position(0, 700);

  // When the button is clicked change_background()
  // function is called
  button.mouseClicked(startPlaying);
}

// function writeTeX() {
//   let equation = createTeX(
//     "{v_{\\rm ф}} = \\omega/k"
//   );
//   equation.position(20, 150);
//   equation.size(25);
//   equation.stroke(false);
//   equation.fill(color('rgb(255,0,0)'));
//   equation.play("createFill", 0, 0);
// }

function drawArrow(base, vec, size = 7, color = 'black') {
  push();
  vec.x -= base.x;
  vec.y -= base.y;
  stroke(color);
  strokeWeight(3);
  fill(color);
  translate(base.x, base.y);
  line(0, 0, vec.x, vec.y);
  rotate(vec.heading());
  translate(vec.mag() - size, 0);
  triangle(0, size / 2, 0, -size / 2, size, 0);
  pop();
}

function draw() {
  background(220);

  drawModes(L, time);
  drawPulse(L, time);
  if (play) {
    time += dt;
  }
  // drawArrow(createVector(-50, -100), createVector(-50, -150), size=7, color='red');
}