var fps = 30;

function drawPulse(L, ampl, omega, phase = 0) {
  let ni = 150;
  let w = 10;
  let d;
  beginShape();
  for (let z = -L; z < L; z += L / ni) {
    let dz0 = z / w;
    d = ampl * Math.cos(omega * dz0 + phase);
    vertex(d, z);
  }
  endShape();
}

function drawLines(L, phase) {
  background(220);

  translate(width / 2, height / 2);

  stroke(10);
  noFill();
  strokeWeight(2);

  drawPulse(L, 10, 1, phase);
}

let time = 0, dt = 0.2, L = 200;

function setup() {
  createCanvas(320, 480);
  frameRate(fps);

  background(220);
  writeTeX();
}

function writeTeX() {
  let equation = createTeX(
    "{v_{\\rm ф}} = \\omega/k"
  );
  equation.position(20, 150);
  equation.size(25);
  equation.stroke(false);
  equation.fill(color('rgb(255,0,0)'));
  equation.play("createFill", 0, 0);
}

function drawArrow(base, vec, size=7, color='black') {
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
  drawLines(L, time);
  time += dt;
  drawArrow(createVector(-50, -100), createVector(-50, -150), size=7, color='red');
}