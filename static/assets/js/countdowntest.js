const d = new Date();

const weekday = new Array(7);
weekday[0] = "Sunday";
weekday[1] = "Monday";
weekday[2] = "Tuesday";
weekday[3] = "Wednesday";
weekday[4] = "Thursday";
weekday[5] = "Friday";
weekday[6] = "Saturday";


let day = weekday[d.getDay()];

console.log(day)

if (day == weekday[0]) {
  var timez = [[6, 0, "green"], [8, 0, "red"], [10, 0, "purple"], [18, 0, "blue"]];
} else {
  var timez = [[6, 0, "green"], [12, 0, "red"], [18, 0, "blue"]];
}

const times = timez

console.log(times)

const timer = document.getElementById('time');
const mass_time = document.getElementById('mass_time');


  setInterval(function tick() {
     const now = new Date();
     const nextShip = times.find(it => it[0] > now.getHours() || it[0] == now.getHours() &&  it[1] >= now.getMinutes()) || times[0];

    let hours = nextShip[0] - now.getHours();
    let minutes = nextShip[1] - now.getMinutes();

    let mass_hours = nextShip[0];
    let mass_minutes = nextShip[1];

    if(minutes < 0) { minutes += 60; hours -= 1 }
    if(hours < 0) { hours += 24; }

    const seconds = 60 - now.getSeconds();

    if (mass_hours >= 12) {
      var timing = "PM";
    } else {
      var timing = "AM";
    }

    if (mass_minutes == 0) {
      var minz = "00";
    } else {
      var minz = mass_minutes
    }

    timer.innerHTML = `${hours}:${minutes}:${seconds}`;
    timer.style.color = nextShip[2];

    mass_time.innerHTML = `${mass_hours}:${minz} ${timing}`;

  }, 1000);