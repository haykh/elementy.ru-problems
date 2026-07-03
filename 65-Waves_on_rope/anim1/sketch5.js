var fps = 15;

let time = 0, dt = 0.1, L = 200;

function fourier(kx, n) {
  return (1 / n) * sin(n * 2 * PI * kx);
}

function drawSawtooth(L, nmodes) {
  push();
  translate(width / 2, height / 2 + 120);
  stroke(10);
  noFill();
  strokeWeight(2);

  let k = 0.2 * 2 * PI / L;
  let A0 = 100;
  let NRES = 250;

  beginShape();
  for (let x = -1.5 * L; x < 1.5 * L; x += L / NRES) {
    let y = k * x;
    y = A0 * ((y - floor(y)));
    vertex(x, y);
  }
  endShape();

  if (nmodes > 0) {
    stroke(250, 0, 0);
    beginShape();
    for (let x = -1.5 * L; x < 1.5 * L; x += L / NRES) {
      let y0 = k * x;
      let y = 0;
      for (let n = 1; n <= nmodes; n++) {
        y += fourier(y0, n);
      }
      y = A0 * (0.5 - (1 / PI) * y);
      vertex(x, y);
    }
    endShape();

    stroke(0, 100, 250);
    translate(0, -370);
    for (let n = 1; n <= nmodes; n++) {
      translate(0, 300 / nmodes);
      beginShape();
      for (let x = -1.5 * L; x < 1.5 * L; x += L / NRES) {
        let y0 = k * x;
        let y = fourier(y0, n);
        y = A0 * (0.5 - (1 / PI) * y);
        vertex(x, y / 2);
      }
      endShape();
    }
  }
  pop();
}

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

function draw() {
  background(220);
  let n = min(parseInt(time), 40);
  drawSawtooth(L, n);
  if (play) {
    time += dt;
    dt += 0.002;
  }
    // push();
    // translate(width / 2, height / 2);
    noStroke();
    fill(0);
    textSize(32);
    text(`n = ${n}`, 20, 40);
  // pop();
}